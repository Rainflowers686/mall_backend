# 🛒 Mall Backend (商城核心后端)

本项目是一个基于 **Django 4.x** + **Django REST Framework (DRF)** 构建的现代化、前后端分离的电商系统后端 API 服务。
完全对标《商城系统任务书》的各项硬性指标，为移动端（React Native/Vue 等）提供稳定、安全、高可用的业务接口。

## ✨ 核心特性 (Features)
- **🔐 坚固的安全防线**：基于 `djangorestframework-simplejwt` 实现的 JWT 令牌双重身份认证。
- **🛍️ 智能购物车**：支持商品数量的无缝拦截与自动累加聚合。
- **⚡ 史诗级交易引擎**：基于 `@transaction.atomic` 数据库事务护盾的一键结算 API，确保算价、扣库存、清空购物车、生成订单多步操作“同生共死”。
- **🌐 跨域无障碍**：已配置完备的 CORS 策略，完美兼容多端跨域调用。
- **💬 客服留言系统**：提供完整的用户留言与在线客服数据流转。
- **📦 订单状态机**：支持 待支付 -> 待发货 -> 待收货 -> 已完成/已取消 的完整生命周期流转。

## 📁 核心交付物说明 (Deliverables)
本项目严格按照交付标准提供了以下文件：
1. **源码包**：包含 `requirements.txt` 完整依赖清单。
2. **数据库脚本**：根目录下的 `init_mall_database.sql` (包含完整的表结构与测试数据)。
3. **接口定义文档**：根目录下的 `schema.yml` (OpenAPI 3.0 规范导出文件)，同时内置了 Swagger UI 交互式在线文档。

---

## 🚀 部署说明书 (Deployment Guide)

### 1. 环境准备
```bash
# 进入项目目录
cd mall_backend

# 激活虚拟环境并安装所有依赖
pip install -r requirements.txt
```

### 2. 数据库初始化 (⚠️ 极其重要)
本项目无需手动执行 migrate 建表，请直接导入提供的 SQL 脚本以获取完整的结构和初始数据。
请确保本地已安装 MySQL 8.0+。

```bash
# 1. 登录本地 MySQL
mysql -u root -p

# 2. 创建空数据库 (数据库名需与 settings.py 中的配置一致，例如 mall)
CREATE DATABASE mall CHARACTER SET utf8mb4;
EXIT;

# 3. 将交付的 SQL 脚本导入数据库
mysql -u root -p mall < init_mall_database.sql
```

### 4. 启动服务
```bash
python manage.py runserver
```

---

## 🗂️ 接口文档与后台入口 (API Docs & Admin)

服务启动后，可通过浏览器访问以下核心入口：

* **📚 交互式 API 接口文档 (Swagger UI)**: `http://127.0.0.1:8000/api/docs/` 
  *(前端开发对接必备！可直接在网页内查看所有请求参数、返回格式，并进行接口测试)*
* **⚙️ 系统管理后台 (Django Admin)**: `http://127.0.0.1:8000/admin/` 
  *(用于管理员进行商品上下架、修改订单状态为“待发货”等核心操作)*

---
*Developed with passion by Rain (Li Yurun).*