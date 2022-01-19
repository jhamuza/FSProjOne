# config/urls.py
from django.contrib import admin
from . import views
from django.urls import path,include, re_path
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    re_path(r"^dashboard/", views.dashboard, name="dashboard"),
    #re_path(r"^dashboard/", dashboard, name="dashboard"),
    #path('Page2/', page2PageView.as_view(), name="Page2"),
    path('infobanjir/', views.infobanjir, name='innfobanjir') #Connecting the path views to the page, in this case, page2
]