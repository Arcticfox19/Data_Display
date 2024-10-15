from flask import Blueprint, request, render_template, current_app
from sqlalchemy import desc
from applications.common.utils.http import table_api
from applications.common.utils.rights import authorize
from applications.models.admin_log import Answering
from applications.schemas.admin_log import AnsweringSchema
from applications.common.curd import model_to_dicts
from applications.common.utils.validate import str_escape
from applications.common.helper import ModelFilter
from flask_login import current_user

bp = Blueprint('log', __name__, url_prefix='/log')


# 日志管理
@bp.get('/')
@authorize("system:log:main")
def index():
    return render_template('system/admin_log/main.html')


# # 登录日志
# @bp.get('/loginLog')
# @authorize("system:log:main")
# def login_log():
#     # orm查询
#     # 使用分页获取data需要.items
#     log = AdminLog.query.filter_by(url='/passport/login').order_by(desc(AdminLog.create_time)).layui_paginate()
#     count = log.total
#     return table_api(data= model_to_dicts(schema=LogOutSchema, data=log.items), count=count)


#   日志分页查询
@bp.get('/loginLog')
@authorize("system:log:main")
def data():
    if current_user.username == current_app.config.get("SUPERADMIN"):
        # 获取请求参数
        Name = str_escape(request.args.get("Name"))
        PaintingName = str_escape(request.args.get('PaintingName'))
        # 查询参数构造
        mf = ModelFilter()
        if Name:
            mf.contains(field_name="Name", value=Name)
        if PaintingName:
            mf.contains(field_name="PaintingName", value=PaintingName)
        # orm查询
        # 使用分页获取data需要.items
        answering = Answering.query.filter(mf.get_filter(Answering)).layui_paginate()
        count = answering.total
        # 返回api
        return table_api(data=model_to_dicts(schema=AnsweringSchema, data=answering.items), count=count)
    else:
        # 获取请求参数
        Name = current_user.realname
        # print(current_user.username)
        # 查询参数构造
        mf = ModelFilter()
        if Name:
            mf.contains(field_name="Name", value=Name)
        # orm查询
        # 使用分页获取data需要.items
        answering = Answering.query.filter(mf.get_filter(Answering)).layui_paginate()
        count = answering.total
        # 返回api
        return table_api(data=model_to_dicts(schema=AnsweringSchema, data=answering.items), count=count)



# 操作日志
@bp.get('/operateLog')
@authorize("system:log:main")
def operate_log():
    # orm查询
    # 使用分页获取data需要.items
    log = AdminLog.query.filter(
        AdminLog.url != '/passport/login').order_by(
        desc(AdminLog.create_time)).layui_paginate()
    count = log.total
    return table_api(data=model_to_dicts(schema=LogOutSchema, data=log.items), count=count)
