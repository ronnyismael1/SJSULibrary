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

Create admin login with
```sh
python manage.py createsuperuser
```

Keep it simple for demonstration purposes.
USER: rismael
PASS: password

For creating the html and css I used a lot of bootstrap templates.