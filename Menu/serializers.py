from rest_framework import serializers
from Menu.models import FoodClassification,Dishes

class FoodClassificationSerializers(serializers.ModelSerializer):
	class Meta:
		model = FoodClassification
		fields = '__all__'	


class DishesSerializers(serializers.ModelSerializer):
	classification_name = serializers.CharField(source="classification.name",read_only = True)

	class Meta:
		model = Dishes
		fields = '__all__'	
