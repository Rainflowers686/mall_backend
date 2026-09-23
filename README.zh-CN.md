# Geek Mall Backend

[English](README.md) | 简体中文

本仓库是 Geek Mall 课程项目的 Django REST Framework API。源码按 goods、products、trade 和 users 等 Django 应用组织。

## 本地运行

创建并启用 Python 虚拟环境，安装依赖，配置本地数据库，然后在仓库根目录启动 Django：

~~~powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py runserver
~~~

使用前应检查数据库初始化材料和本地设置。不要公开凭据或私人数据库内容。

## 仓库内容

- goods/、products/、trade/、users/：应用模块
- mall_backend/：Django 项目配置
- requirements.txt：Python 依赖
