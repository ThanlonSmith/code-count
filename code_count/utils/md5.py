# -*- coding:utf-8 -*-
# @Time : 2019/8/25 18:31
# @Author : Thanlon
# @Email : thanlon@sina.com
# @File : md5.py
# @Project : code_count
import hashlib
from settings import Config


def md5(password):
    hash = hashlib.md5(Config.SALT)
    # hash.update(b'thanlon')
    hash.update(bytes(password, encoding='utf-8'))
    return hash.hexdigest()
# print(md5('123456'))