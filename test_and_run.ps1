# 定义默认的端口号
param (
    [int]$Port = 8000  # 默认的 Django 服务端口号
)

# 检查本地是否有 3306 端口正在使用
Write-Host "检查 3306 端口是否被占用..."
$portInUse = netstat -ano | Select-String ":3306"

if ($portInUse) {
    Write-Host "检测到 3306 端口已被占用，可能已有 MySQL 服务运行。" -ForegroundColor Green
} else {
    # 检查是否安装了 docker-compose
    Write-Host "3306 端口未被占用，检查是否安装了 docker-compose..."
    $dockerComposeInstalled = Get-Command "docker-compose" -ErrorAction SilentlyContinue

    if (-not $dockerComposeInstalled) {
        Write-Host "未检测到 docker-compose，请安装 MySQL 或 docker-compose 后重试。" -ForegroundColor Red
        exit 1
    }

    # 如果 docker-compose 存在，则尝试启动 docker-compose 文件
    Write-Host "检测到 docker-compose，尝试启动 MySQL 容器..."
    try {
        docker-compose -f "./docker-compose-demo.yml" up -d
        Write-Host "MySQL 容器已成功启动。" -ForegroundColor Green
    } catch {
        Write-Host "启动 docker-compose 时出错：" -ForegroundColor Red
        Write-Host $_.Exception.Message
        exit 1
    }
}

# 检查是否安装了 Poetry
Write-Host "检查是否安装了 Poetry..."
$poetryInstalled = Get-Command "poetry" -ErrorAction SilentlyContinue

if (-not $poetryInstalled) {
    Write-Host "未检测到 Poetry，请安装 Poetry 后重试。" -ForegroundColor Red
    exit 1
}

# 检查 Poetry 是否已配置虚拟环境
Write-Host "检测 Poetry 是否已安装依赖并配置虚拟环境..."
try {
    poetry check
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Poetry 环境未正确配置，尝试安装依赖..."
        poetry install --no-root
    }
    Write-Host "Poetry 环境检测完成。" -ForegroundColor Green
} catch {
    Write-Host "Poetry 配置时出错：" -ForegroundColor Red
    Write-Host $_.Exception.Message
    exit 1
}

# 如果本地 3306 有服务或者 docker-compose 成功启动，执行 Django 命令
Write-Host "准备执行 Django 管理命令..." -ForegroundColor Cyan

try {
    # 将模型的变更转换为数据库迁移文件
    Write-Host "执行 poetry run python manage.py makemigrations..."
    poetry run python manage.py makemigrations

    # 执行数据库迁移
    Write-Host "执行 poetry run python manage.py migrate..."
    poetry run python manage.py migrate

    # 启动 Django 的开发服务器
    Write-Host "启动 Django 开发服务器，监听端口 $Port..."
    poetry run python manage.py runserver 0.0.0.0:$Port
} catch {
    Write-Host "执行 Django 管理命令时出错：" -ForegroundColor Red
    Write-Host $_.Exception.Message
    exit 1
}
