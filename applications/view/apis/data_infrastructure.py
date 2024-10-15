from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from flask_sqlalchemy.pagination import Pagination
from sqlalchemy import desc

from applications.common import curd
from applications.common.curd import enable_status, disable_status
from applications.common.utils.http import table_api, fail_api, success_api
from applications.common.utils.paginate import paginate
from applications.common.utils.rights import authorize
from applications.common.utils.validate import str_escape
from applications.extensions import db
from sqlalchemy import text

# 数据设施基础

bp = Blueprint('data_infrastructure', __name__, url_prefix='/data_infrastructure')


# 北京市移动电话通话时长--查询
@bp.get('/list')
def data_list():
    page = request.args.get('page', type=int)
    limit = request.args.get('limit', type=int)
    select_year = request.args.get('select_year',default='', type=int)

    # result = [
    #              {'id': 1, 'inComeHours': 8677726.7, 'outGoHours': 4522793.3, 'year': 2022, },
    #              {'id': 2, 'inComeHours': 9061741.7, 'outGoHours': 4775394.3, 'year': 2021, },
    #              {'id': 3, 'inComeHours': 9580053.6, 'outGoHours': 5118773.4, 'year': 2020, },
    #          ] * 10

    # 查库表
    sql = "select * from call_duration"
    if select_year:
        sql+=f' where year={select_year}'
    sql += f' order by year desc'
    results = db.session.execute(text(sql))
    column_names = results.keys()
    result_json = [dict(zip(column_names,item)) for item in results]

    page_data = paginate(data=result_json, page=page, page_size=limit)

    data_json = {
        'code': 0,
        'msg': None,
        'page': page,
        'pageSize': limit,
        'count': len(result_json),
        'data': page_data['data']
    }
    return jsonify(data_json)



# 北京市移动电话通话时长--更新
@bp.post('/updateOrCreate')
def updateOrCreate():
    id = request.form.get('id', type=int)
    outGoHours = request.form.get('outGoHours', type=float)
    inComeHours = request.form.get('inComeHours',default='', type=float)
    year = request.form.get('year',default='', type=int)

    # 构建 SQL 更新语句
    if id:
        sql = f"UPDATE call_duration SET outGoHours = {outGoHours}, inComeHours = {inComeHours}, year = {year} WHERE id = {id}"
        tag = '更新'
    else:
        sql = f"INSERT INTO call_duration (outGoHours, inComeHours, year) VALUES ({outGoHours}, {inComeHours}, {year})"
        tag = "新增"

    try:
        # 执行 SQL 更新语句
        db.session.execute(text(sql))
        db.session.commit()

        data_json = {
            'code': 0,
            'success':True,
            'msg': f"{tag}成功！"
        }
    except Exception as e:
        data_json = {
            'code': 1,
            'success': False,
            'msg': f"{tag}失败"
        }

    return jsonify(data_json)

# 北京市移动电话通话时长--更新
@bp.post('/delete')
def delete():
    id = request.form.get('id', type=int)

    # 构建 SQL 删除语句
    sql = "DELETE FROM call_duration WHERE id = :id"
    params = {'id': id}

    try:
        # 执行 SQL 删除语句
        db.session.execute(text(sql), params)
        db.session.commit()

        data_json = {
            'code': 0,
            'msg': "删除成功！"
        }
    except Exception as e:
        data_json = {
            'code': 1,
            'msg': "删除失败"
        }

    return jsonify(data_json)
