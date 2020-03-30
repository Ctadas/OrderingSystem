from rest_framework import serializers
from Menu.models import FoodClassification,Dishes
from rest_framework.pagination import PageNumberPagination

class FoodClassificationSerializers(serializers.ModelSerializer):
	class Meta:
		model = FoodClassification
		fields = '__all__'	


class DishesSerializers(serializers.ModelSerializer):
	classification_name = serializers.CharField(source="classification.name",read_only = True)

	class Meta:
		model = Dishes
		fields = '__all__'	

class StandardResultsSetPagination(PageNumberPagination):
	# 默认每页显示的数据条数
	page_size = 10
	# 获取URL参数中设置的每页显示数据条数
	page_size_query_param = 'page_size'
	# 获取URL参数中传入的页码key
	page_query_param = 'page'

