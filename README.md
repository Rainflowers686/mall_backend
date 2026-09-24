# Geek Mall Backend

*A focused Django REST API for a university mall coursework build.*

![Python](https://img.shields.io/badge/Python-API-3776AB?logo=python&logoColor=white) ![Django REST Framework](https://img.shields.io/badge/Django-REST%20Framework-092E20?logo=django&logoColor=white) ![Status](https://img.shields.io/badge/Status-Course%20Project-586069)

**Guide:** [Status](#project-status) · [Run locally](#run-locally) · [Repository contents](#repository-contents)

[English](README.md) | [简体中文](README.zh-CN.md)

This repository contains the Django REST Framework API for the Geek Mall coursework project. The source is organized into Django apps for goods, products, trade and users.

## Project status

Course project. The repository keeps the API source and local setup notes for reference.

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
