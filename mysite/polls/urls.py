from . import views
from django.urls import path

urlpatterns = [
    path('latha', views.index, name='index'),
    path('php', views.send_ls, name='ls')
    ]