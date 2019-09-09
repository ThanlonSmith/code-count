from settings import Config
import pymysql


def fetchone(sql, args):
    conn = Config.POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def fetch_all(sql, args):
    conn = Config.POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def insert(sql, args):
    '''
    向数据库中插入数据
    :param sql: 执行插入的sql语句
    :param args: 其它参数
    :return: 受影响的行数
    '''
    conn = Config.POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    row = cursor.execute(sql, args)
    conn.commit()
    cursor.close()
    conn.close()
    return row
