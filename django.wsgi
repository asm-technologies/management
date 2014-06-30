import os
import sys

sys.path.append('/var/www/management')
sys.path.append('/var/www/management/mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'



path = '/var/www/management/mysite'
if path not in sys.path:
    sys.path.append(path)


import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
