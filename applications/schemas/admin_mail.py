from applications.extensions import ma
from marshmallow import fields
from applications.models import User

# # 用户models的序列化类 检查邮件对象的 user_id 属性，如果不为 None，则通过查询数据库来获取相应用户的真实姓名，并将其返回
# class MailOutSchema(ma.Schema):
#     id = fields.Integer()
#     receiver = fields.Str()
#     subject = fields.Str()
#     content = fields.Str()
#     realname = fields.Method("get_realname")
#     create_at = fields.DateTime()
#
#     def get_realname(self, obj):
#         if obj.user_id != None:
#             return User.query.filter_by(id=obj.user_id).first().realname
#         else:
#             return None


class MailOutSchema(ma.Schema):
    Name = fields.String()
    PhoneNumber = fields.String()
    PSQI_score = fields.Integer()
    anxiety_score = fields.Integer()
    depression_score = fields.Integer()