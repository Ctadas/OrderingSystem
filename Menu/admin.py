from django.contrib import admin
from Menu.models import FoodClassification,Dishes

class FoodClassificationAdmin(admin.ModelAdmin):
	pass

class DishesAdmin(admin.ModelAdmin):
	pass


admin.site.register(FoodClassification, FoodClassificationAdmin)
admin.site.register(Dishes, DishesAdmin)