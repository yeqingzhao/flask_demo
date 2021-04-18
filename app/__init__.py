# -*- coding: utf-8 -*-
"""
@File    : manage.py
@Create  : 2021/04/18
@Author  : yeqingzhao
"""
from flask import Flask

from app.modules.views import external_api


def create_app():
    # 创建 app
    flask_app = Flask(__name__)
    flask_app.config.update({'JSON_AS_ASCII': Flask})  # 配置为utf-8
    flask_app.register_blueprint(external_api)  # 注册蓝图

    return flask_app
