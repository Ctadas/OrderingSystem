from rest_framework import serializers
from Menu.models import FoodClassification,Dishes

class DishesSerializers(serializers.ModelSerializer):
	classification = serializers.CharField(source="classification.name",read_only = True)

	class Meta:
		model = Dishes
		fields = '__all__'	
