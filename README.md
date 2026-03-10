# 🛒 Mall Backend (商城核心后端)



本项目是一个基于 **Django 4.x** + **Django REST Framework (DRF)** 构建的现代化、前后端分离的电商系统后端 API 服务。
为移动端 App（如 React Native / Expo）和 Web 前端提供稳定、安全、高可用的核心业务接口。

## ✨ 核心特性 (Features)

- **🔐 坚固的安全防线**：基于 `djangorestframework-simplejwt` 实现的 JWT 令牌双重身份认证。
- **🛍️ 智能购物车**：支持商品数量的无缝拦截与自动累加聚合。
- **⚡ 史诗级交易引擎**：基于 `@transaction.atomic` 数据库事务护盾的一键结算 API，确保算价、扣库存、清空购物车、生成订单多步操作“同生共死”，零数据异常。
- **🌐 跨域无障碍**：已配置完备的 CORS 策略，完美兼容多端跨域调用。
- **📦 优雅的接口设计**：全面采用 DRF `ModelViewSet` 和 `DefaultRouter`，RESTful 风格拉满。

## 🛠️ 技术栈 (Tech Stack)

- **核心框架**：Python 3.10+ / Django 4.2 / Django REST Framework
- **数据库**：MySQL 8.0+ (PyMySQL + cryptography)
- **图像处理**：Pillow
- **跨域支持**：django-cors-headers

## 🚀 快速启动 (Quick Start)

### 1. 克隆与环境配置
```bash
# 进入项目目录
cd mall_backend

# 激活虚拟环境 (Windows)
.\.venv\Scripts\activate

# 安装所有依赖包
pip install -r requirements.txt