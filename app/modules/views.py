# -*- coding: utf-8 -*-
"""
@File    : manage.py
@Create  : 2021/04/18
@Author  : yeqingzhao
"""
from flask import Blueprint
from flask import jsonify
from flask import request

external_api = Blueprint("external_api", __name__)  # 设置蓝图


@external_api.route('/hello', methods=['POST'])
def hello():
    data = request.json

    return jsonify({'status': 'success', 'data': data})
