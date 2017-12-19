from flask import render_template

from . import controller
from ..model.models import Tester


@controller.route('/', methods=['GET'])
def index_index():
    # data=Tester(name="testuser",info="only for add test")
    # db.session.add(data)
    # db.session.commit()
    testers = Tester.query.filter_by(name='testuser').all()
    return render_template('index/index.html', testers=testers)
