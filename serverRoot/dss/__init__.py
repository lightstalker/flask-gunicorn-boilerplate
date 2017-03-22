from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dss:dss@localhost/dss'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import dss.views

# from flask_httpauth import HTTPBasicAuth
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.automap import automap_base
# from collections import OrderedDict
#todo readup on https://flask-restless.readthedocs.io/en/stable/basicusage.html, will simplify this process further (couldnt use on translation as no idea on column names frontend wise)