# _*_ coding: utf-8 _*_

from datetime import datetime
from app import db

class Content(db.Model):
    __tablename__ = "content"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    title = db.Column(db.String(100), unique=True)  # 标题
    content = db.Column(db.Text)  # 内容
    img_url = db.Column(db.Text)  # 图片
    tag = db.Column(db.Text)
    addtime = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    uuid = db.Column(db.Integer, unique=True)  # 唯一标识符

    def __repr__(self):
        return "<Title %r>" % self.title

