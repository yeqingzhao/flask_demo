# -*- coding: utf-8 -*-
"""
@File    : manage.py
@Create  : 2021/04/18
@Author  : yeqingzhao
"""
from app import create_app

app = create_app()  # 创建应用工厂实例

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8800, debug=True)