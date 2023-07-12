from django.contrib import admin
from django.urls import path,include
from . import views
import requests
urlpatterns = [
    path('up/',views.upload),
    path('projects/<str:pk1>/<str:pk2>',views.get),
    path('login/',views.login),
    path('projects/<str:pk1>/<str:pk2>/<int:pk3>',views.get1),
    path('projects/<str:pk>',views.get_run),
    path('projects/',views.projects),
]