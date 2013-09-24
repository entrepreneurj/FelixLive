import os
import sys	
sys.path.append('/web')
os.environ['DJANGO_SETTINGS_MODULE'] = 'liveblog.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
