# -*- coding:utf-8 -*-
# @Time : 2019/8/25 17:28
# @Author : Thanlon
# @Email : thanlon@sina.com
# @File : test.py
# @Project : code_count
# import hashlib
#
# hash = hashlib.md5(b'123456')
# hash.update(b'123456')
# ret = hash.hexdigest()
# print(ret)


'''
连接数据库
'''
# import pymysql
#
# conn = pymysql.Connect(host='localhost', user='root', password='wwwnxl',
#                        database='codecount')  # 如果中文不能显示，设置charset = 'utf8'
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 设置拿到的是字典，不设置是元组
# # 不要自己去拼接
# # sql = "select *from userinfo where user = '%s' and pwd = '%s'" % (
# # "thanl' or 1=1-- ", '63d7d0d52449193ba1f1321cd8b89a62')
#
# # cursor.execute('select *from userinfo where user = %s and pwd = %s',
# #                ("thanlon", '63d7d0d52449193ba1f1321cd8b89a62'))
# cursor.execute('select *from userinfo where user = %(us)s and pwd = %(pw)s',
#                {'us': "thanlon", 'pw': '63d7d0d52449193ba1f1321cd8b89a62'})
# # data = cursor.fetchall()
# data = cursor.fetchone()  # 匹配成功的第一条数据,如果失败，返回None
# print(data)
# cursor.close()
# conn.close()

# 解压文件
import shutil

shutil._unpack_zipfile(r'/home/thanlon/PycharmProjects/code_count/files/flask.zip','/home/thanlon/PycharmProjects/code_count/files/')
