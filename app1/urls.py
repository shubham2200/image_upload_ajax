from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home , name= "home"),
    path('save_data' , save_data , name="save_data")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)