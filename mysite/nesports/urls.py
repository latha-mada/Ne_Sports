from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.images, name='index'),
    path('patriots', views.patriots, name='patriots'),
    path('celtics', views.celtics, name='celtics'),
    path('bruins', views.bruins, name='bruins'),
    path('redsox', views.redsox, name='redsox'),
    url(r'(?P<num>[0-9]+)/$', views.random, name='random'),
    path('analyze', views.analyze, name='analyze'),
    path('analyzem', views.analyzem, name='analyzem'),

    ]


# url(r'index', views.images, name='index'),
#     url(r'index/.*(?P<num>[0-9]+)/$', views.random, name='random'),
#     url(r'index/patriots', views.patriots, name='patriots')