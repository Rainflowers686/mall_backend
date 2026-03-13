# 🛒 Geek Mall Backend
### 商城核心后端 API 系统

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![DRF](https://img.shields.io/badge/DRF-API-red)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange)
![JWT](https://img.shields.io/badge/Auth-JWT-yellow)
![Swagger](https://img.shields.io/badge/API-Swagger-blue)
![License](https://img.shields.io/badge/license-MIT-green)


<p align="center">
现代化电商系统后端 | Django + DRF + JWT | 前后端分离架构
</p>

---

# 📖 项目简介

**Geek Mall Backend** 是一个基于 **Django 4.x** 与 **Django REST Framework (DRF)** 构建的现代化电商后端系统。

该项目采用 **前后端完全分离架构**，为 Web / 移动端（Vue / React / React Native / 小程序等）提供 **标准化 RESTful API 服务**。

系统实现了完整的电商核心业务逻辑，包括：

- 用户认证系统
- 商品管理系统
- 购物车系统
- 订单交易系统
- 收货地址系统
- 客服留言系统
- 后台商品与订单管理系统

项目严格遵循 **RESTful API 设计规范**，并通过 **JWT Token 机制**实现安全认证。

**协作说明：**  
本项目为 **“极客商城”全栈系统的后端部分**。  
配套的 **Vue3 前端项目源码同样存放于我的 GitHub 仓库中**，前后端需要配合运行才能实现完整的电商业务流程。

---

# 🧱 技术架构 (Tech Stack)

| 技术 | 说明 |
|-----|-----|
| **Python 3.10+** | 后端开发语言 |
| **Django 4.x** | Web 应用框架 |
| **Django REST Framework** | REST API 开发框架 |
| **MySQL 8.0** | 关系型数据库 |
| **SimpleJWT** | JWT 身份认证 |
| **Django Admin** | 管理后台 |
| **SimpleUI** | Admin UI 增强 |
| **drf-spectacular** | OpenAPI / Swagger 文档 |

---

# 🏗️ 系统架构

```
                 ┌──────────────┐
                 │  Frontend    │
                 │ Vue / RN / H5│
                 └──────┬───────┘
                        │ REST API
                        ▼
               ┌──────────────────┐
               │ Django REST API  │
               │  Mall Backend    │
               └────────┬─────────┘
                        │
         ┌──────────────┼──────────────┐
         ▼              ▼              ▼
     用户系统        商品系统        订单系统
     Users           Products        Orders

                        │
                        ▼
                 ┌───────────┐
                 │  MySQL 8  │
                 └───────────┘
```

---

# ✨ 核心特性 (Features)

## 🔐 安全认证系统
基于 **JWT Token 双令牌认证机制**

- Access Token
- Refresh Token
- Token 自动刷新

所有 API 均需要身份认证访问。

---

## 🛍️ 智能购物车系统

购物车支持：

- 商品自动累加
- 数量自动合并
- 一键删除
- 批量结算

确保用户购物流程顺畅。

---

## ⚡ 原子级订单交易系统

核心结算 API 使用：

```python
@transaction.atomic
```

保证以下操作 **事务一致性**：

```
计算价格
↓
扣减库存
↓
生成订单
↓
清空购物车
```

若任何一步失败，系统将 **自动回滚数据库**。

---

## 📦 订单状态机

订单生命周期：

```
待支付
   ↓
待发货
   ↓
待收货
   ↓
已完成

（任意阶段）
   ↓
已取消
```

系统自动维护合法状态流转。

---

## 🌐 跨域支持 (CORS)

已配置完整跨域策略：

```
django-cors-headers
```

支持：

- Web 前端
- 移动端
- 小程序
- 第三方客户端

---

## 💬 客服留言系统

用户可提交：

- 咨询
- 建议
- 售后问题

后台管理员可查看并处理。

---

# 📦 核心交付物 (Deliverables)

本项目严格按照交付标准提供：

### 1️⃣ 项目源码

包含完整依赖清单：

```
requirements.txt
```

---

### 2️⃣ 数据库初始化脚本

```
init_mall_database.sql
```

包含：

- 完整表结构
- 初始测试数据

---

### 3️⃣ OpenAPI 接口文档

```
schema.yml
```

符合 **OpenAPI 3.0 规范**

并自动生成：

- Swagger UI
- 接口在线测试

---

# 🚀 部署指南 (Deployment Guide)

## 1️⃣ 克隆项目

```bash
git clone https://github.com/yourname/mall_backend.git
cd mall_backend
```

---

## 2️⃣ 创建虚拟环境

```bash
python -m venv .venv
```

激活环境：

### Windows

```bash
.venv\Scripts\activate
```

### Linux / Mac

```bash
source .venv/bin/activate
```

---

## 3️⃣ 安装依赖

```bash
pip install -r requirements.txt
```

---

## 4️⃣ 数据库初始化 (⚠️重要)

本项目 **不使用 migrate 自动建表**。

请直接导入 SQL：

```bash
mysql -u root -p
```

```sql
CREATE DATABASE mall CHARACTER SET utf8mb4;
```

导入脚本：

```bash
mysql -u root -p mall < init_mall_database.sql
```

---

## 5️⃣ 启动服务

```bash
python manage.py runserver
```

默认地址：

```
http://127.0.0.1:8000
```

---

# 📚 API 文档

启动项目后访问：

### Swagger UI

```
http://127.0.0.1:8000/api/docs/
```

支持：

- 接口参数查看
- 在线测试 API
- 自动生成文档

---

# ⚙️ 管理后台

管理员后台：

```
http://127.0.0.1:8000/admin/
```

后台功能：

- 商品管理
- 订单管理
- 用户管理
- 留言管理
- 商品上下架
- 库存管理

---

# 🗂️ 项目结构

```
mall_backend
│
├─ mall_backend        # Django 项目配置
│
├─ users               # 用户系统
├─ products            # 商品系统
├─ cart                # 购物车系统
├─ orders              # 订单系统
├─ addresses           # 收货地址
├─ messages            # 客服留言
│
├─ init_mall_database.sql
├─ schema.yml
├─ requirements.txt
├─ manage.py
└─ README.md
```

---

# 🔐 API 认证方式

登录成功后返回：

```
access_token
refresh_token
```

调用 API 时需要：

```
Authorization: Bearer <access_token>
```

示例：

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI...
```

---

# 📊 项目亮点

✔ 完整电商后端架构  
✔ 标准 RESTful API 设计  
✔ JWT Token 安全认证  
✔ 原子事务订单系统  
✔ OpenAPI 自动文档  
✔ Django Admin 管理后台  

适合作为：

- 🎓 计算机课程设计
- 💼 后端实习项目
- 📚 Django 学习项目
- 🚀 全栈开发练习

---

# 👨‍💻 Author

**Rain (Li Yurun)**

- Backend Developer
- Computer Science Student

GitHub:

```
https://github.com/Rainflowers686
```

---

# ⭐ License

This project is for **learning and academic purposes only**.
