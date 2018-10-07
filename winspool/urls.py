from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #url(r'^$', views.index, name='index'),
    #url(r'summary/$', view.summary, name='summary')
    #path('', views.index, name='index'),
    path('summary/', views.summary, name='summary'),
    path('details/', views.details, name='details')
]
