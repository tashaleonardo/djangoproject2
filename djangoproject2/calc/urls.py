from django.urls import path
from . import views

urlpatterns = [
    path('', views.calc_list, name='calc_list'),
 ]
