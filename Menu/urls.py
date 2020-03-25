from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Menu.views import 	DishesList,DishesDetail

urlpatterns = [
	path('dishes/', DishesList.as_view()),
	path('dishes/<int:pk>/', DishesDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)