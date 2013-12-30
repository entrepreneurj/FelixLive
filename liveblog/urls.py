from django.conf.urls import patterns, url, include
from django.core.urlresolvers import reverse
#from blog.models import *
from blog import views 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^liveblog/', include('liveblog.foo.urls')),
	url(r'^$', views.home, name="home"),
	url(r'^api/content/', views.get_content, name="get_content"),
#url(r'^$', home, name="home"),
    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
)
