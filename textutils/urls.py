
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('https://github.com/Satyamtripathi1996/textutils/edit/master/textutils/urls.py', views.index, name='index'),
    path('https://github.com/Satyamtripathi1996/textutils/edit/master/textutils/urls.py', views.analyze, name='analyze'),
]
