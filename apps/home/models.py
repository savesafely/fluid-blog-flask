import peewee as pw
from exts import db
from datetime import datetime

class BlogModel(pw.Model):
    __tablename__ = 'blog'
    id = pw.AutoField()
    title = pw.CharField(verbose_name='标题',max_length=100,null=False)
    content = pw.TextField(verbose_name='内容',null=False)
    create_time = pw.DateTimeField(verbose_name='创建时间',default=datetime.utcnow())

    class meta:
        database = db  # 这里是数据库链接，为了方便建立多个表，可以把这个部分提炼出来形成一个新的类
        table_name = 'blog'  # 这里可以自定义表名






# Field Type	Sqlite	Postgresql	MySQL
# IntegerField 	integer 	integer 	integer
# BigIntegerField 	integer 	bigint 	bigint
# SmallIntegerField 	integer 	smallint 	smallint
# AutoField 	integer 	serial 	integer
# FloatField 	real 	real 	real
# DoubleField 	real 	double precision 	double precision
# DecimalField 	decimal 	numeric 	numeric
# CharField 	varchar 	varchar 	varchar
# FixedCharField 	char 	char 	char
# TextField 	text 	text 	longtext
# BlobField 	blob 	bytea 	blob
# BitField 	integer 	bigint 	bigint
# BigBitField 	blob 	bytea 	blob
# UUIDField 	text 	uuid 	varchar(40)
# DateTimeField 	datetime 	timestamp 	datetime
# DateField 	date 	date 	date
# TimeField 	time 	time 	time
# TimestampField 	integer 	integer 	integer
# IPField 	integer 	bigint 	bigint
# BooleanField 	integer 	boolean 	bool
# BareField 	untyped 	not supported 	not supported
# ForeignKeyField 	integer 	integer 	integer
# null = False – 可否为空
# index = False – index索引
# unique = False – unique索引
# column_name = None – string representing the underlying column to use if different, useful for legacy databases
# default = None – 默认值，如果callable, 会调用生成！
# primary_key = False – 主键
# constraints = None - a list of one or more constraints, e.g. [Check('price > 0')]
# sequence = None – sequence to populate field (if backend supports it)
# collation = None – collation to use for ordering the field / index
# unindexed = False – indicate field on virtual table should be unindexed (SQLite-only)
# choices = None – an optional iterable containing 2-tuples of value, display
# help_text = None – string representing any helpful text for this field
# verbose_name = None – string representing the “user-friendly” name of this field