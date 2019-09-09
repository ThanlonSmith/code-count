# -*- coding:utf-8 -*-
# @Time : 2019/8/25 16:13
# @Author : Thanlon
# @Email : thanlon@sina.com
# @File : manage.py
# @Project : code_count
from code_count import create_app

app = create_app()
if __name__ == '__main__':
    app.debug = True
    app.run()
