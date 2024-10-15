import datetime
from applications.extensions import db

class AdminLog(db.Model):
    __tablename__ = 'admin_admin_log'
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(10))
    uid = db.Column(db.Integer)
    url = db.Column(db.String(255))
    desc = db.Column(db.Text)
    ip = db.Column(db.String(255))
    success = db.Column(db.Integer)
    user_agent = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

class Answering(db.Model):
    __tablename__ = 'answering_data'
    DataID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    PaintingName = db.Column(db.String(255))
    IsAnswerCorrect = db.Column(db.String(255))
    ReactionTime = db.Column(db.Float)
