from exts import db
from datetime import datetime

class BlogModel(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text(1000),nullable=False)
    create_time = db.Column(db.DATETIME,default=datetime.utcnow())


    def __init__(self,title,content):
        self.title = title
        self.content = content


