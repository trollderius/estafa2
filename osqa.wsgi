import os
import sys
sys.path.append('/var/www/estafa2')
sys.path.append('/var/www/estafa2/osqa')

# os.environ['DJANGO_SETTINGS_MODULE'] = 'osqa.settings'
os.environ['PYTHON_EGG_CACHE'] = '/var/www/estafa2/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
