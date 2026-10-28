<div align="center">

# **Geek Mall Backend**

Geek Mall 课程项目的 Django REST Framework 后端。

提供商品、账号、购物车和订单接口，使用 JWT 登录，并保留接口文档与数据库初始化材料。

![Python](https://img.shields.io/badge/Python-API-3776AB?logo=python&logoColor=white) ![Django REST Framework](https://img.shields.io/badge/Django-REST%20Framework-092E20?logo=django&logoColor=white) ![Status](https://img.shields.io/badge/Status-Course%20Project-586069)

[English](README.md) · [简体中文](README.zh-CN.md)

[项目状态](#项目状态) · [本地运行](#本地运行) · [API 入口](#api-入口) · [仓库内容](#仓库内容) · [参与贡献](CONTRIBUTING.md)

</div>

## 项目状态

课程项目，Django 应用包括 `goods`、`trade` 与 `users`；`products/` 保存商品图片。仓库保留 API 源码和本地配置资料，正式部署需要单独检查运行配置与安全设置。

## 本地运行

创建并启用 Python 虚拟环境，安装已记录的依赖：

~~~powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py runserver
~~~

执行最后一条命令前，先检查 `mall_backend/settings.py`，创建或选择本地数据库。准备全新的开发库时，使用 `python manage.py migrate` 应用迁移。导入 `init_mall_database.sql` 前应阅读其内容；含有需要保留的数据时，不要直接执行初始化脚本。凭据和私人数据库内容不要提交到公开仓库。

## API 入口

| 范围 | 入口 |
| --- | --- |
| 商品 | `/api/products/` |
| 登录与令牌刷新 | `/api/login/`、`/api/token/refresh/` |
| 账号、地址与留言 | `/api/register/`、`/api/addresses/`、`/api/messages/` |
| 购物车与订单 | `/api/cart/`、`/api/orders/` |
| OpenAPI 与 Swagger UI | `/api/schema/`、`/api/docs/` |

路由定义见 [mall_backend/urls.py](mall_backend/urls.py)，配套前端见 [mall_frontend](https://github.com/Rainflowers686/mall_frontend)。

## 仓库内容

- [goods/](goods/)、[trade/](trade/) 与 [users/](users/)：Django 应用模块。
- [mall_backend/](mall_backend/)：设置与 URL 配置。
- [products/](products/)：示例商品图片。
- [requirements.txt](requirements.txt)：锁定的 Python 依赖。
- [schema.yml](schema.yml) 与 [test_api.http](test_api.http)：接口参考和请求示例。

## 贡献与安全

本地检查见 [CONTRIBUTING.md](CONTRIBUTING.md)，凭据和权限问题见 [SECURITY.md](SECURITY.md)。涉及写数据的修改应使用可丢弃的测试数据库。

## 许可与数据

仓库尚未提供覆盖全部内容的使用许可。课程资料、商品图片和数据库样例可能有各自的权利归属；再分发前应确认授权，共享测试材料前应移除个人数据。
