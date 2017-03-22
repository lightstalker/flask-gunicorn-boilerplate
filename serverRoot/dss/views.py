from dss import app, models
from models import db, Test
from flask_restless import APIManager

manager = APIManager(app, flask_sqlalchemy_db=db)

@app.route('/')
def hello_world():
    try:
        value = Test.query.all()[-1].data
    except:
        value = "none"

    return 'Hello, World! TEST \n'\
        'last data added {}'.format(value)

manager.create_api(Test, methods=['GET', 'POST'])
