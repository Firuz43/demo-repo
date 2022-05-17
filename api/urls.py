from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiView, name="home"),
    path('create/', views.addItem, name="addItem"),
    path('')
]
