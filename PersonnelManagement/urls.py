from django.contrib import admin
from django.urls import path
from PersonnelManagement import views

urlpatterns = [
    path('weixin_login/', views.weixin_login),
]