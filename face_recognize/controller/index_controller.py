from flask import render_template

from . import controller


@controller.route('/', methods=['GET'])
def index_index():
    return render_template('deep_id/index.html')
