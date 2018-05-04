import json
import os
import uuid

from flask import request

from . import controller


# from .. import db
# from ..model.models import Image, DeepidRecord


@controller.route('/deepid/validate', methods=['POST'])
def deep_id_img_validate():
    file1 = request.files['file1']
    file2 = request.files['file2']
    file1_base_name = str(uuid.uuid4()).replace('-', '') + os.path.splitext(file1.filename)[-1]
    file2_base_name = str(uuid.uuid4()).replace('-', '') + os.path.splitext(file2.filename)[-1]
    from .. import app_config
    file1_name = os.path.join(app_config['FILE_BASE_PATH'] + '/image/deep_id', file1_base_name)
    file2_name = os.path.join(app_config['FILE_BASE_PATH'] + '/image/deep_id', file2_base_name)
    file1.save(file1_name)
    file2.save(file2_name)
    from .. import deep_id_validator
    result, val = deep_id_validator.validate(file1_name, file2_name)
    if val is None:
        os.remove(file1_name)
        os.remove(file2_name)
        return json.dumps({'status': False, 'message': '请上传较为明显的人脸图片', 'result': None}, ensure_ascii=False)
    # record = db.engine.execute(
    #     'select max(record_index) from deepid_record')
    # record_data = [(dict(row.items())) for row in record]
    # print(record_data)
    # if record_data[0]['max(record_index)'] is None:
    #     cur_id = 1
    # else:
    #     cur_id = int(record_data[0]['max(record_index)']) + 1
    # print(cur_id)
    # new_dir = app_config['FILE_BASE_PATH'] + '/image/deep_id/' + str(cur_id)
    # os.mkdir(new_dir)
    # file1_new_name = new_dir + '/' + file1_base_name
    # file2_new_name = new_dir + '/' + file2_base_name
    # shutil.move(file1_name, file1_new_name)
    # shutil.move(file2_name, file2_new_name)
    # image1 = Image(url=file1_new_name)
    # image2 = Image(url=file2_new_name)
    # deepid_record = DeepidRecord(record_index=cur_id)
    # db.session.add(image1)
    # db.session.add(image2)
    # db.session.add(deepid_record)
    # db.session.commit()
    # return json.dumps({'status': True, 'message': '上传成功', 'result': result, 'id': cur_id}, ensure_ascii=False)
    return json.dumps({'status': True, 'message': '上传成功', 'result': result}, ensure_ascii=False)
