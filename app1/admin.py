from django.contrib import admin
from .models import *


# Register your models here.
class imageAdmin(admin.ModelAdmin):
    list_display = ('id','user_name')
admin.site.register(user_image , imageAdmin )