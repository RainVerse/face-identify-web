from flask import render_template

from . import controller


@controller.route('/admin', methods=['GET'])
def admin_index():
    return render_template('admin/index.html')
