# config/urls.py
from cgi import test
from django.contrib import admin
from . import views
from django.urls import path,include, re_path
from home.views import dashboard, register
from django.contrib.staticfiles.storage import staticfiles_storage
#from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'), 
    re_path(r"^dashboard/", dashboard, name="dashboard"), #if i changed this, it'll affect the path for the views
    re_path(r"^register/", register, name="register"),
    path('irrigation/', views.irrigation, name="irrigation"),  #Connecting the path views to the page, in this case, irrigation.html
    path('infobanjir/', views.infobanjir, name='infobanjir'),
    path('references/', views.ref, name="references"),
    path('files/', views.csvfiles, name="files"),
    re_path(r"^test/", test, name="test"),

]