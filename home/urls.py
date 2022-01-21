# config/urls.py
from django.contrib import admin
from . import views
from django.urls import path,include, re_path
from home.views import dashboard, register
#from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'), #the authentication works, as long as there's no overlapping users
    re_path(r"^dashboard/", dashboard, name="dashboard"), #if i changed this, it'll affect the path for the views
    re_path(r"^register/", register, name="register"), #changed from re_path to this
    #re_path(r"^dashboard/", dashboard, name="dashboard"),
    #path('Page2/', page2PageView.as_view(), name="Page2"),
    path('infobanjir/', views.infobanjir, name='infobanjir') #Connecting the path views to the page, in this case, page2
]