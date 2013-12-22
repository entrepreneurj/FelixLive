from django.contrib import admin
from liveblog.blog.models import *


class EventAdmin(admin.ModelAdmin):
	pass

admin.site.register(Event,EventAdmin)
admin.site.register(Author)
admin.site.register(Content)
