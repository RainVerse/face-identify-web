import os.path
import pickle

import cv2
import numpy as np
import tensorflow as tf


class deep_id_validator(object):
    def __init__(self, model_base_path):
        self.model_base_path = model_base_path
        self.cascade_file = model_base_path + '/haarcascade/haarcascade_frontalface_alt.xml'
        print(self.cascade_file)
        if not os.path.isfile(self.cascade_file):
            raise RuntimeError("%s: not found" % self.cascade_file)
        saver = tf.train.import_meta_graph(model_base_path + "/deep_id/25000.ckpt.meta")
        self.deep_id_session = tf.Session()
        self.input = tf.get_default_graph().get_tensor_by_name('input/x:0')
        self.op_validate = tf.get_default_graph().get_tensor_by_name('DeepID1/validate:0')
        saver.restore(self.deep_id_session, model_base_path + '/deep_id/25000.ckpt')
        self.A = pickle.load(open(model_base_path + '/joint_bayesian/A.pkl', 'rb'))
        self.G = pickle.load(open(model_base_path + '/joint_bayesian/G.pkl', 'rb'))

    def detect(self, filename):
        cascade_file = self.cascade_file
        cascade = cv2.CascadeClassifier(cascade_file)
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = cascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=3,
                                         minSize=(47, 55))
        print(len(faces))
        if len(faces) != 1:
            return None
        for i, (x, y, w, h) in enumerate(faces):
            face = image[y: y + h, x:x + w, :]
            face = cv2.resize(face, (47, 55))
            return face

    def verify(self, x1, x2):
        x1.shape = (-1, 1)
        x2.shape = (-1, 1)
        ratio = np.dot(np.dot(np.transpose(x1), self.A), x1) + np.dot(np.dot(np.transpose(x2), self.A),
                                                                      x2) - 2 * np.dot(np.dot(np.transpose(x1), self.G),
                                                                                       x2)
        return float(ratio)

    def validate(self, image1, image2):
        pic1 = self.detect(image1)
        pic2 = self.detect(image2)
        if pic2 is None or pic1 is None:
            return False, None
        pic1arr = np.reshape(np.asarray(pic1, dtype='float32'), [1, 55, 47, 3])
        pic2arr = np.reshape(np.asarray(pic2, dtype='float32'), [1, 55, 47, 3])
        h1 = self.deep_id_session.run(self.op_validate, {self.input: pic1arr})
        h2 = self.deep_id_session.run(self.op_validate, {self.input: pic2arr})
        result = self.verify(h1, h2)
        if result >= -17.65:
            return True, result
        else:
            return False, result
