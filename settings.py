# -*- coding:utf-8 -*-
# @Time : 2019/8/25 16:15
# @Author : Thanlon
# @Email : thanlon@sina.com
# @File : settings.py
# @Project : code_count
from DBUtils.PooledDB import PooledDB, SharedDBConnection
import pymysql


class Config(object):
    SALT = b'123456'
    SECRET_KEY = 'THANLON'
    MAX_CONTENT_LENGTH = 1024 * 1024 * 10  # 控制上传文件的大小为10MB，413错误
    POOL = PooledDB(
        creator=pymysql,  # 使用连接数据库的模块
        maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
        mincached=2,  # 初始化时，连接池中至少创建的控线连接，0表示不创建
        maxcached=5,  # 连接池中最多闲置的连接，0和None表示不限制，超过闲置数会被关闭
        maxshared=3,  # 连接池中最多共享的连接数量，0和None。pymysql和mysqldb等模块的threadsafety都是1，所以在这里是无效的
        blocking=True,  # 连接池中如果没有可用的连接，是否阻塞等待，True:等待，False:不等待报错`
        maxusage=None,  # 一个连接被重复使用的次数，None表示无限制
        setsession=[],  # 开始会话前执行的命令列表，执行sql之前先发一些命令，可以写一些sql命令
        # ping mysql服务端，检查是否可用，如果0和None表示不检查，1是每次请求(连接数据库)的时候,默认是1；2表示创建cursor的时候检查；4：执行cursor的execute方法检查；7表示总是检查
        ping=0,
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='codecount',
        charset='utf8'
    )
