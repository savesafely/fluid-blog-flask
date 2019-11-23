# coding: utf8
# from flask_sqlalchemy import SQLAlchemy
from app import app,db
from app.models import Content
# db = SQLAlchemy()
# db.init_app(app)
db.create_all()

for i in range(1,25):
    content = Content(
        title=f"又一家数据公司被查{i}",
        content="9 月 6 日下午，多位业内人士称，杭州知名大数据服务公司杭州魔蝎数据科技有限公司，疑似被相关执法人员控制，其中一位周姓核心高管人员被警方带走。\
                以上是前几天技术圈传播的一则新闻，又一家数据公司被调查，很多数据从业者、爬虫开发者发出了“感叹” —— 「爬虫用得好，XX进得早；数据玩得溜，XX吃个够」。\
                魔蝎科技作为一家数据服务公司，曾在 2017 年一篇『爬虫凶猛：爬支付宝、爬微信、窃取现金贷放贷数据』的文章中，被指出存在开发使用恶意爬虫的行为。\
                当然关于魔蝎科技为什么被查，这个等待执法部门的调查结果即可，咱们不在这里无端猜测。\
                我今天要说的是关于爬虫的合法性，我希望通过一些案例来探讨：怎样做一个不触碰红线的爬虫开发者。",
        img_url="https://timgsa.baidu.com/timg?image&quality=80",
        tag="爬虫",
        uuid=i
    )
    db.session.add(content)
    db.session.commit()