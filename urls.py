from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView



urlpatterns = [
    path('winspool/', include(('winspool.urls', 'winspool'), namespace="winspool")),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='main.html'), name='main'),
    #re_path(r'^winspool/login/$', auth_views.LoginView,{'template_name':"winspool/login.html"}),
    #re_path(r'^winspool/logout/$', auth_views.LogoutView,{'next_page': '/winspool/login/'}),
    path('winspool/', include('django.contrib.auth.urls')),
    #re_path(r'^winspool/logout/$', auth_views.LogoutView,{'next_page': '/winspool/login/'}),


]
