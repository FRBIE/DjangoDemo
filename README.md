# Demo
## 推荐运行方式
为了简化项目的运行流程，我们推荐使用脚本 test_and_run.ps1，该脚本可以自动完成以下任务：

- 检查本地环境（MySQL 端口、docker-compose、Poetry）。
- 如果 MySQL 未运行，启动 Docker 容器中的 MySQL 服务。
- 自动安装依赖并配置虚拟环境。
- 启动 Django 服务（默认监听端口为 8000，可通过参数自定义）。

使用方法
确保本机已安装以下工具：
- PowerShell 7+
- Docker Compose
- Poetry
运行脚本：
```powershell
pwsh .\test_and_run.ps1 -Port 8080
```

如果不指定 -Port，默认端口为 8000。
## 项目结构
- Demo（主项目)
- api

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

**2、配置项目**

项目使用 Poetry 管理依赖
```bash
# 安装 Poetry：
pip install poetry
# 安装项目依赖：
poetry install --no-root
# 激活虚拟环境：
poetry shell

# 依赖更新：
# 如果新增或更新了依赖，请确保运行以下命令更新 poetry.lock 文件：
poetry add <package-name>
```



项目初次运行项目或模型变更时：配置好数据库后，生成迁移文件并应用到数据库。
```bash
# 将模型的变更（例如新增字段、修改字段、删除字段等）转换为数据库迁移文件
python manage.py makemigrations
# 执行数据库迁移操作，根据生成的迁移文件，更新实际数据库的结构
python manage.py migrate
```

在模型没有更改的情况下，只需要指定端口 启动服务
```bash
# 启动 Django 的开发服务器 
# 0.0.0.0：表示服务器绑定到本地所有可用的 IP 地址，允许在局域网内访问。
# 8000：默认端口号，可以更改为其他端口（如 8080）。
python manage.py runserver 0.0.0.0:8000
```




## JWT说明

用户存在表`auth_user`中