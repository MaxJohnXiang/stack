# -*- coding:utf-8 -*-
from flask import Flask
from .config import FlaskConfig
app= Flask(__name__)
app.config.from_object(FlaskConfig)
app.config['SECRET_KEY'] = '123456'


app.config.update(SECRET_KEY='123456')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True