


#  Fluid Blog Flask


## Features
- [x] 自动同步博客
- [x] 自动部署githubhub page


## 使用
```
uwsgi:

uwsgi uwsgi.ini

gunicorn:

gunicorn -c gunicorn.py run:app

```


##安装环境
```bash
 sudo pip3 install -r requirements.txt --trusted-host mirrors.aliyun.com -i http://mirrors.aliyun.com/pypi/simple/ 
 ```

 ##自动生成模块
 ```
python -m pwiz -e sqlite test.db > test.py
 ```