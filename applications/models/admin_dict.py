import datetime
from applications.extensions import db


class DictType(db.Model):
    __tablename__ = 'admin_dict_type'
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(255), comment='字典类型名称')
    type_code = db.Column(db.String(255), comment='字典类型标识')
    description = db.Column(db.String(255), comment='字典类型描述')
    enable = db.Column(db.Integer, comment='是否开启')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')


class DictData(db.Model):
    __tablename__ = 'admin_dict_data'
    id = db.Column(db.Integer, primary_key=True)
    data_label = db.Column(db.String(255), comment='字典类型名称')
    data_value = db.Column(db.String(255), comment='字典类型标识')
    type_code = db.Column(db.String(255), comment='字典类型描述')
    is_default = db.Column(db.Integer, comment='是否默认')
    enable = db.Column(db.Integer, comment='是否开启')
    remark = db.Column(db.String(255), comment='备注')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now, comment='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')

class Audio(db.Model):
    __tablename__ = 'audio_data'
    DataID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), comment='姓名')
    PaintingName = db.Column(db.String(255), comment='画作名')
    AudioUrl = db.Column(db.String(255), comment='音频地址')
    AudioWave = db.Column(db.String(255), comment='波形图地址')
