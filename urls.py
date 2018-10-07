from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('winspool/', include(('winspool.urls', 'winspool'), namespace="winspool")),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='main.html'), name='main'),
    path('winspool/login', auth_views.LoginView,{'template_name':"winspool/login.html"}, name='login'),
    path('winspool/logout', auth_views.LogoutView,{'next_page': "winspool/login.html"}),
    #path('winspool/password_reset', auth_views.PasswordResetView,{'template': "registration/password_reset_form.html"}),
    path('winspool/', include('django.contrib.auth.urls')),
]
