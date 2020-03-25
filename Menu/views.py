from django.shortcuts import render
from Menu.models import Dishes
from Menu.serializers import DishesSerializers
from rest_framework import mixins
from rest_framework import generics

class DishesList(mixins.ListModelMixin,
				  generics.GenericAPIView):
	queryset = Dishes.objects.all()
	serializer_class = DishesSerializers

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

class DishesDetail(mixins.RetrieveModelMixin,
					mixins.UpdateModelMixin,
					mixins.DestroyModelMixin,
					generics.GenericAPIView):
	queryset = Dishes.objects.all()
	serializer_class = DishesSerializers

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		print(args,kwargs)
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)