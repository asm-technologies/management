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

===========================================================================================================================

Move to Production Environment:
OS: Cent OS 

Django can run using wsgi (similar to cgi-bin)
Check apachea has wsgi_module has already installed by the command apachectl -M. It will display all installed modules. If you don't find wsgi_module please install using the following command,

yum install mod_wsgi

Also install the dependent development packages,

yum install python-devel  ## python development package to compile and install pip packages

Deploy Steps:
cd /var/www/
git clone https://github.com/asm-technologies/management.git
cd management
pip install -r requirements.txt

Apache configuration in /etc/httpd/conf/http.conf:

WSGIScriptAlias /management "/var/www/management/django.wsgi"
Alias /static "/var/www/management/mysite/static"
Alias /site_media "/var/www/management/mysite/site_media"

<Directory "/var/www/management/">
    AllowOverride None
    Options None
    Order allow,deny
    Allow from all
</Directory>




