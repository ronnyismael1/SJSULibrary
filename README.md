# Setup
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
```

Create admin login with
```sh
python manage.py createsuperuser
```

# Login
Keep it simple for demonstration purposes.
USER: admin
PASS: password

# Exploring the Project
Launch the website with
```sh
python manage.py runserver
```

Login with the admin credentials and feel free to explore!

Admin panel will be
<http://127.0.0.1:8000/admin>
