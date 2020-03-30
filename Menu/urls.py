from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Menu import views

urlpatterns = [
	path('dishes_management/', views.dishes_management),
	path('dishes/', views.DishesList.as_view()),
	path('dishes/<int:pk>', views.DishesDetail.as_view()),
	path('dishes_page/', views.DisheListPage.as_view()),
	path('food_classification/', views.FoodClassificationList.as_view()),
	path('food_classification/<int:pk>', views.FoodClassificationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)