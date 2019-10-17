from peewee import *

database = SqliteDatabase('test.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Blog(BaseModel):
    content = TextField()
    create_time = DateTimeField(null=True)
    title = CharField()

    class Meta:
        table_name = 'blog'

