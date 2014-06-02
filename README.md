Management-project-ASM 
=====================

This project is designed to manage all Employee details of an organization . Has graph,employee and project details.

Uses django-pinax module


Installing and Getting Started:

    pip install virtualenv
    virtualenv management-env             ## create a directory where virtual environment will run and all dependent libraries will be available
    source management-env/bin/activate   ## Now you will be inside virutal environment & Type deactivate to deactivate virtual env
    
    
============================================================================================================================

Clone source code :
	
	git clone https://github.com/asm-technologies/management.git
	cd management
	pip install -r requirements.txt     #install all dependent modules
	python manage.py syncdb				## to sync flat file db
	python manage.py runserver		    ## Now type localhost:8000 in local browser to view site
