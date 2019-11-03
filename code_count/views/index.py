# -*- coding:utf-8 -*-
# @Time : 2019/8/25 19:28
# @Author : Thanlon
# @Email : thanlon@sina.com
# @File : index.py
# @Project : code_count
from flask import render_template, Blueprint, session, redirect, request
import os, uuid
from settings import Config
from ..utils import helper

bp_index = Blueprint('index', __name__)


@bp_index.before_request
def process_request():
    if not session.get('user_info'):
        return redirect('/login')


# @bp_index.route('/index')
# def index():
#     title = {'title': '欢迎使用代码统计系统!'}
#     return render_template('index.html', title=title)


@bp_index.route('/')
def user_list():
    title = {'title': '用户列表'}
    sql = 'select id,user,nickname from userinfo'
    args = []
    data_list = helper.fetch_all(sql, args)
    return render_template('user_list.html', title=title, data_list=data_list)


@bp_index.route('/detail/<int:nid>')  # 默认nid是string类型
def detail(nid):
    sql = 'select id,line,ctime from record where user_id = %s'
    args = nid
    record_list = helper.fetch_all(sql, args)
    # print(record_list)
    data_list = []
    time_list = []
    for row in record_list:
        data_list.append(row['line'])
        time_list.append(float(row['ctime'].strftime("%m.%d")))  # datetime类型转换成字符串
    title = {'title': '提交代码详情页面'}
    return render_template('detail.html', title=title, record_list=record_list, data_list=data_list,
                           time_list=time_list, )


@bp_index.route('/upload', methods=['get', 'post'])  # 默认nid是string类型
def upload():
    title = {'title': '代码上传'}
    msg = ''
    if request.method == 'GET':
        return render_template('upload.html', title=title)
    file_obj = request.files.get('code')  # <FileStorage: '' ('application/octet-stream')>,把上传的东西方内存了
    # print(file_obj.filename)  # 上传的文件名(带扩展名)
    # print(file_obj.stream)  # 文件的内容被封装到对象中
    # 1.检查上传文件的后缀名
    filename_ext = file_obj.filename.rsplit('.', maxsplit=1)  # 元组
    if len(filename_ext) != 2:
        msg = '请上传压缩文件!'
        return render_template('upload.html', msg=msg, title=title)
    if filename_ext[1] != 'zip':
        msg = '请上传后缀名为zip的文件'
        return render_template('upload.html', msg=msg, title=title)

    # 2.接受用户上传的文件并写入到服务器本地
    file_path = os.path.join('files', file_obj.filename)
    file_obj.save(file_path)  # save的本质是：从file_obj.stream中读取内容写入到文件
    # 3.解压zip文件
    import shutil
    target_path = os.path.join('files', str(uuid.uuid4()))  # 允许上传的文件名相同
    # print(target_path)#files/549fb0e2-924c-460d-a993-935fcc8e3274
    # 通过open打开i压缩文件，读取内容再进行解压
    shutil._unpack_zipfile(file_path, target_path)

    # 2和3步合并，接受用户上传的文件，并解压至指定目录
    # import shutil
    # shutil._unpack_zipfile(file_obj.stream, r'/home/thanlon/PycharmProjects/code_count/files')
    # 4. 遍历目录下的所有文件
    # for item in os.listdir(target_path):
    #     print(item)
    # for item in os.walk(target_path):
    #     # 每一个item是一个元组，每一个元组有三个元素，分别是当前路径、当前路径下所有文件夹、当前路径下的所有文件
    #      print(item)  # ('files/79d81a3d-455f-4124-ba24-7d7b8a990c4a/keymaps', [], ['Default Proper Redo.xml'])
    sum_num = 0
    for base_path, folder_list, file_list in os.walk(target_path):
        for file_name in file_list:
            file_path = os.path.join(base_path, file_name)
            # print(file_path)  # files/b39a2b87-69b3-4094-942a-58103e70b8a6/options/databaseDrivers.xml
            file_ext = file_path.rsplit('.', 1)
            if len(file_ext) != 2:
                continue
            if file_ext[1] != 'py':
                continue
            file_num = 0
            with open(file_path, 'rb') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    if line.startswith(b'#'):
                        continue
                    file_num += 1
            # print(file_num, file_path)  # 每一个文件行数
            sum_num += file_num
    # print(sum_num)
    # 获取当前时间
    import datetime
    # ctime = datetime.datetime.now()
    ctime = datetime.date.today()  # 当前日期
    # print(sum_num, ctime, session['user_info']['id'])
    '''
    插入数据之前需要查询今天是否已经提交
    '''
    sql = 'select id from record where ctime = %s and user_id = %s'
    args = (ctime, session['user_info']['id'])
    data = helper.fetchone(sql, args)
    if data:
        return '今天的代码已经上传了!'
    sql = 'insert record(line,ctime,user_id) values(%s,%s,%s)'
    args = (sum_num, ctime, session['user_info']['id'])
    helper.insert(sql, args)
    return '上传成功!'
