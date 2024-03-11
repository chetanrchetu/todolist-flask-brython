from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
# from flask_cors import CORS
import os

DATABASE_PATH=f'{os.getcwd()}\\website\\mydatabase.db'

app=Flask(__name__,template_folder=r'D:\Learn\Flask\Todo\website\templates',static_folder=r'D:\Learn\Flask\Todo\website\static')

app.config['SECRET_KEY']='1234567890'

app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DATABASE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)

from website.views import views 
app.register_blueprint(views)




