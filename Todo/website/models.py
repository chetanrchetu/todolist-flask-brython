from website import db 
import json

class Taskdb(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    task=db.Column(db.String(1000),nullable=False,unique=True)

