import os.path
import pickle

import cv2
import numpy as np
import tensorflow as tf


def detect(filename, model_base_path):
    cascade_file = model_base_path + '/haarcascade/haarcascade_frontalface_alt.xml'
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=3,
                                     minSize=(47, 55))
    for i, (x, y, w, h) in enumerate(faces):
        face = image[y: y + h, x:x + w, :]
        face = cv2.resize(face, (47, 55))
        return face


def verify(A, G, x1, x2):
    x1.shape = (-1, 1)
    x2.shape = (-1, 1)
    ratio = np.dot(np.dot(np.transpose(x1), A), x1) + np.dot(np.dot(np.transpose(x2), A), x2) - 2 * np.dot(
        np.dot(np.transpose(x1), G), x2)
    return float(ratio)


def validate(image1, image2, model_base_path):
    pic1 = detect(image1, model_base_path)
    pic2 = detect(image2, model_base_path)
    pic1arr = np.reshape(np.asarray(pic1, dtype='float32'), [1, 55, 47, 3])
    pic2arr = np.reshape(np.asarray(pic2, dtype='float32'), [1, 55, 47, 3])

    saver = tf.train.import_meta_graph(model_base_path + "/deep_id/25000.ckpt.meta")
    with tf.Session() as sess:
        input = tf.get_default_graph().get_tensor_by_name('input/x:0')
        validate = tf.get_default_graph().get_tensor_by_name('DeepID1/validate:0')
        saver.restore(sess, model_base_path + '/deep_id/25000.ckpt')
        h1 = sess.run(validate, {input: pic1arr})
        h2 = sess.run(validate, {input: pic2arr})
    with open(model_base_path + '/joint_bayesian/A.pkl', 'rb') as f:
        A = pickle.load(f)
    with open(model_base_path + '/joint_bayesian/G.pkl', 'rb') as f:
        G = pickle.load(f)
    result = verify(A, G, h1, h2)
    if result >= -17.65:
        return True, result
    else:
        return False, result


if __name__ == '__main__':
    result, val = validate('../../test/test1.jpg', '../../test/test2.jpg')
    print(result)
