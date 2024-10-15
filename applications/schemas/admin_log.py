from applications.extensions import ma
from marshmallow import fields

class AnsweringSchema(ma.Schema):
    DataID = fields.Integer()
    Name = fields.Str()
    PaintingName = fields.Str()
    IsAnswerCorrect = fields.Str()
    ReactionTime = fields.Float()

class LogOutSchema(ma.Schema):
    id = fields.Integer()
    method = fields.Str()
    uid = fields.Str()
    url = fields.Str()
    desc = fields.Str()
    ip = fields.Str()
    user_agent = fields.Str()
    success = fields.Bool()
    create_time = fields.DateTime()