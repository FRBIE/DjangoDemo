# Demo

## 项目结构

- Demo（主项目)
- api
- venv

## 项目运行

**1、Mysql数据库配置**

在`Demo.settings.py中`修改以下配置

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'demo',  # 数据库名
        'USER': 'root',       # 数据库用户名
        'PASSWORD': 'Xrp220903',   # 数据库密码
        'HOST': 'localhost',           # 数据库主机地址，默认是本地
        'PORT': '3306',                # 数据库端口号，MySQL 默认是 3306
    }
}
```

**2、运行命令**

python manage.py makemigrations

python manage.py migrate

python manage.py runserver 0.0.0.0:8000





## JWT说明

用户存在表`auth_user`中