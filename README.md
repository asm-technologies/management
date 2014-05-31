Management-project-ASM 
=====================

This project is designed to manage all Employee details of an organization . Has graph,employee and project details.

Uses django-pinax module


Usage:

    django-admin.py startproject --template=https://github.com/pinax/pinax-project-account/zipball/master <project_name>

Getting Started:

    pip install virtualenv
    virtualenv mysiteenv
    source mysiteenv/bin/activate
    pip install Django==1.6.2
    django-admin.py startproject --template=https://github.com/pinax/pinax-project-account/zipball/master mysite
    cd mysite
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py runserver
