from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Tutorial)
admin.site.register(Video)
admin.site.register(Article)
admin.site.register(Like)
admin.site.register(Comment)