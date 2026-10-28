# Geek Mall Backend

*大学课程商城项目的 Django REST API。*

![Python](https://img.shields.io/badge/Python-API-3776AB?logo=python&logoColor=white) ![Django REST Framework](https://img.shields.io/badge/Django-REST%20Framework-092E20?logo=django&logoColor=white) ![Status](https://img.shields.io/badge/Status-Course%20Project-586069)

**导航：**[状态](#项目状态) · [本地运行](#本地运行) · [仓库内容](#仓库内容)

[English](README.md) | [简体中文](README.zh-CN.md)

本仓库是 Geek Mall 课程项目的 Django REST Framework API。源码按 goods、products、trade 和 users 等 Django 应用组织。

## 项目状态

课程项目仓库，保留 API 源码和本地运行说明。

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
