from django.shortcuts import render
from Menu.models import Dishes,FoodClassification
from django.shortcuts import render
from Menu.serializers import DishesSerializers,FoodClassificationSerializers
from rest_framework import mixins
from rest_framework import generics

def dishes_management(request):
	return render(request, 'menu/index.html')


class FoodClassificationList(mixins.ListModelMixin,
							mixins.CreateModelMixin,
							generics.GenericAPIView):
	queryset = FoodClassification.objects.all()
	serializer_class = FoodClassificationSerializers

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class FoodClassificationDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	queryset = FoodClassification.objects.all()
	serializer_class = FoodClassificationSerializers

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

class DishesList(mixins.ListModelMixin,
				mixins.CreateModelMixin,
				generics.GenericAPIView):
	queryset = Dishes.objects.all()
	serializer_class = DishesSerializers

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class DishesDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	queryset = Dishes.objects.all()
	serializer_class = DishesSerializers

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		print(request.data,args,kwargs)
		return self.partial_update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)