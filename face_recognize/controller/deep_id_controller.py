import json
import os
import uuid

from flask import request

from . import controller


@controller.route('/deepid/validate', methods=['POST'])
def deep_id_img_validate():
    file1 = request.files['file1']
    file2 = request.files['file2']
    file1_name = str(uuid.uuid4()).replace('-', '') + os.path.splitext(file1.filename)[-1]
    file2_name = str(uuid.uuid4()).replace('-', '') + os.path.splitext(file2.filename)[-1]
    from .. import app_config
    file1_name = os.path.join(app_config['FILE_BASE_PATH'] + '/image/deep_id', file1_name)
    file2_name = os.path.join(app_config['FILE_BASE_PATH'] + '/image/deep_id', file2_name)
    file1.save(file1_name)
    file2.save(file2_name)
    from .. import deep_id_validator
    result, val = deep_id_validator.validate(file1_name, file2_name)
    if val is None:
        return json.dumps({'status': False, 'message': '请上传较为明显的人脸图片', 'result': None}, ensure_ascii=False)
    return json.dumps({'status': True, 'message': '上传成功', 'result': result}, ensure_ascii=False)
