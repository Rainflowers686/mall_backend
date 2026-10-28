# Geek Mall Backend

English | [简体中文](README.zh-CN.md)

This repository contains the Django REST Framework API for the Geek Mall coursework project. The source is organized into Django apps for goods, products, trade and users.

## Run locally

Create and activate a Python virtual environment, install the requirements, configure the local database, and then start Django from the repository root:

~~~powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py runserver
~~~

Database initialization and local settings require review before use. Do not publish credentials or private database contents.

## Repository contents

- goods/, products/, trade/, users/ — application modules
- mall_backend/ — Django project configuration
- requirements.txt — Python dependencies
