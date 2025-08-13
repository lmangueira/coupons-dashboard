# Proyecto Django - Coupons

Instructions for running the project manually

## Requirements
- Python 3.13
- Django 5.x
- uv (gestor de entornos/paquetes para Python)
- SQLite (incluido por defecto en Python/Django)

## Quickstart
1) Crate and activate virtual env

```
uv venv
source .venv/bin/activate
```
2) Install dependencies
```
uv sync
```
or
```
uv pip install -r requirements
```

3) Apply migrations
```
(venv) python manage.py migrate
```

4) Populate Database
Bear in midn that this command will delete all existing coupons and load them from `coupons.json`
```
(venv) python manage.py seed_data
```

6) Execute dev server
```
(venv) python manage.py runserver
```
App will be available at: http://127.0.0.1:8000/

