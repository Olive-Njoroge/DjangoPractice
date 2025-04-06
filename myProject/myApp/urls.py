from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v1/', views.v1, name='v1'),
    path('hello_world/', views.hello_world, name='hello_world'),
]