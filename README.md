Creted virtual environment with:
```sh
python -m venv venv
```

Activated virtual environment with:
```sh
.\venv\Scripts\activate
```

Commands to install django and set up files needed:
```sh
pip install django
django-admin startproject sjsul_library .
python manage.py startapp access_control
python manage.py migrate
python manage.py runserver
```
