from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiView, name="home"),
    path('create/', views.addItem, name="addItem"),
    path('all/', views.viewItems, name="view"),
    path('update/<str:pk>', views.updateItems, name="update"),
]
