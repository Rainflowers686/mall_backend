<div align="center">

# **Geek Mall Backend**

The Django REST Framework API for the Geek Mall coursework project.

Connect product browsing, accounts, carts and orders through documented REST endpoints and JWT authentication.

![Python](https://img.shields.io/badge/Python-API-3776AB?logo=python&logoColor=white) ![Django REST Framework](https://img.shields.io/badge/Django-REST%20Framework-092E20?logo=django&logoColor=white) ![Status](https://img.shields.io/badge/Status-Course%20Project-586069)

[English](README.md) · [简体中文](README.zh-CN.md)

[Status](#project-status) · [Run locally](#run-locally) · [API](#api-entry-points) · [Files](#repository-contents) · [Contribute](CONTRIBUTING.md)

</div>

## Project status

Course project with Django apps for `goods`, `trade` and `users`. The `products/` directory stores product images. The repository preserves the API source and local setup materials; production deployment needs a separate configuration and security review.

## Run locally

Create and activate a Python virtual environment and install the recorded dependencies:

~~~powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py runserver
~~~

Before the final command, review `mall_backend/settings.py`, create or select a local database, and apply migrations with `python manage.py migrate` when preparing a fresh development database. Review `init_mall_database.sql` before importing it; do not apply initialization scripts to a database containing work you need to keep. Credentials and private database contents belong outside public commits.

## API entry points

| Area | Entry point |
| --- | --- |
| Products | `/api/products/` |
| Sign-in and refresh | `/api/login/`, `/api/token/refresh/` |
| Accounts and addresses | `/api/register/`, `/api/addresses/`, `/api/messages/` |
| Cart and orders | `/api/cart/`, `/api/orders/` |
| OpenAPI and Swagger UI | `/api/schema/`, `/api/docs/` |

These routes are declared in [mall_backend/urls.py](mall_backend/urls.py). The companion client is [mall_frontend](https://github.com/Rainflowers686/mall_frontend).

## Repository contents

- [goods/](goods/), [trade/](trade/) and [users/](users/): Django application modules.
- [mall_backend/](mall_backend/): settings and URL configuration.
- [products/](products/): example product images.
- [requirements.txt](requirements.txt): pinned Python dependencies.
- [schema.yml](schema.yml) and [test_api.http](test_api.http): API reference and request examples.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for local checks and [SECURITY.md](SECURITY.md) for credential and authorization reports. Use a disposable test database for changes that write data.

## License and data

No repository-wide license grant is present. Course material, product images and database samples may have separate rights. Confirm permission before redistribution and remove personal data from any shared test fixture.
