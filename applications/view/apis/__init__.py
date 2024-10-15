from flask import Flask, Blueprint

from applications.view.apis.data_infrastructure import bp as data_infrastructure_dp


# 创建sys
api_bp = Blueprint('api', __name__, url_prefix='/api')


def register_api_bps(app: Flask):
    # 在admin_bp下注册子蓝图
    api_bp.register_blueprint(data_infrastructure_dp)

    app.register_blueprint(api_bp)
