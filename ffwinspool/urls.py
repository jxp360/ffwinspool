"""ffwinspool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='main.html'), name='main'),
    #path('winspool/', include('winspool.urls',namespace=("winspool", "winspool"))),
    path('winspool/', include(('winspool.urls', 'winspool'), namespace="winspool")),
    re_path(r'^winspool/login/$', auth_views.LoginView,{'template_name':"winspool/login.html"}),
    re_path(r'^winspool/logout/$', auth_views.LogoutView,{'next_page': '/winspool/login/'}),

]
