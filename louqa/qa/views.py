# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template
from ..user import User
qa =Blueprint('qa',__name__,url_prefix='')

@qa.route('/',defaults={'title':None})
@qa.route('/<title>')
def index(title):
    user=User.query.filter().first()
    return render_template("qa/index.html",title=title,tem_str="max")

