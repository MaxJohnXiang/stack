# -*- coding:utf-8 -*-
from ..dbs import db
from sqlalchemy import Column

class User(db.Model):

    __tablename__='user'

    id=Column(db.Integer,primary_key=True)
    name=Column(db.String(32),nullable=False,unique=True)