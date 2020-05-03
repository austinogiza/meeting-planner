
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>', views.details, name='detail'),
    path('meetings/room/', views.room, name='room'),
    path('new/', views.new, name='new'),
]
