# -*- coding:utf-8 -*-
# @Time : 2019/8/25 16:12
# @Author : Thanlon
# @Email : thanlon@sina.com
# @File : __init__.py
# @Project : code_count
from flask import Flask
from .views.account import account
from .views.index import bp_index


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings.Config')
    app.register_blueprint(account)  # 注意：注册的是蓝图对象，不是py文件
    app.register_blueprint(bp_index)
    return app
