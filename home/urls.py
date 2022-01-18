# config/urls.py
from django.contrib import admin
from . import views
from home.dash_apps.finished_apps import simpleexample #change view here
#from django.conf.urls import url
from django.urls import path,include
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
]