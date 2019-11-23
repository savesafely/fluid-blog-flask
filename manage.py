# coding:utf8
from flask_migrate import Migrate, MigrateCommand
from app import app
from app.models import db
from flask_script import Manager, Server

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')


manage = Manager(app)

# 启动命令
manage.add_command("runserver", Server(use_debugger=True))

# 迁移
Migrate(app,db)
manage.add_command('db',MigrateCommand)


if __name__ == "__main__":
    manage.run()

'''
初始化
python manage.py db init

创建迁移
python manage.py db migrate

执行迁移
python manage.py db upgrade
'''
