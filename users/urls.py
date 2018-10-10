__author__ = 'Pooja'


from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),

]
