# -*- coding:utf-8 -*-
# @Time : 2019/8/25 16:18
# @Author : Thanlon
# @Email : thanlon@sina.com
# @File : account.py
# @Project : code_count
from flask import Blueprint, render_template, request, session, redirect
from ..utils.md5 import md5
from ..utils import helper

account = Blueprint('account', __name__)


@account.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('user')
    password = request.form.get('password')
    '''
    对密码进行加密
    '''
    pwd_md5 = md5(password)
    '''
    数据库中进行校验
    '''
    sql = 'select id,nickname from userinfo where user = %s and pwd = %s'
    args = (username, pwd_md5)
    data = helper.fetchone(sql, args)
    if not data:
        return render_template('login.html', error='用户名或密码错误')
    # session['user_id'] = data['id']
    # session['user_nickname'] = data['nickname']
    # session['user_info'] = {'user_id': data['id'], 'user_nickname': data['nickname']}
    session['user_info'] = data
    return redirect('/')


@account.route('/logout')
def logout():
    if 'user_info' in session:
        del session['user_info']
    return redirect('/')
