from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('winspool/', include ('winspool.urls')),
    path('admin/', admin.site.urls),
]
