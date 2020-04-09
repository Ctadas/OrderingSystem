from django.contrib import admin
from django.urls import path,include,re_path
from Menu import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'food_classification', views.FoodClassificationViewSet)
router.register(r'dishes', views.DishesViewSet)
router.register(r'dishes_page', views.DishesPageViewSet)

urlpatterns = [
	path('dishes_management/', views.dishes_management),
	# path('dishes/', views.DishesList.as_view()),
	# path('dishes/<int:pk>', views.DishesDetail.as_view()),
	# path('dishes_page/', views.DisheListPage.as_view()),
	re_path(r'^', include(router.urls)),
	# path('food_classification/', views.FoodClassificationList.as_view()),
	# path('food_classification/<int:pk>', views.FoodClassificationDetail.as_view()),
]
