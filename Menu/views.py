from django.shortcuts import render
from Menu.models import Dishes,FoodClassification
from django.shortcuts import render
from Menu.serializers import DishesSerializers,FoodClassificationSerializers,StandardResultsSetPagination
from rest_framework import mixins,generics,viewsets

def dishes_management(request):
	return render(request, 'menu/index.html')


class FoodClassificationViewSet(viewsets.ModelViewSet):
	queryset = FoodClassification.objects.all()
	serializer_class = FoodClassificationSerializers 

class DishesViewSet(viewsets.ModelViewSet):
	queryset = Dishes.objects.all()
	serializer_class = DishesSerializers 


class DishesPageViewSet(viewsets.ModelViewSet):
	queryset = Dishes.objects.all()
	serializer_class = DishesSerializers 
	pagination_class = StandardResultsSetPagination

# class FoodClassificationList(mixins.ListModelMixin,
# 							mixins.CreateModelMixin,
# 							generics.GenericAPIView):
# 	model = FoodClassification
# 	serializer_class = FoodClassificationSerializers

# 	def get_queryset(self, *args, **kwargs):
# 		return self.model.objects.all()

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)

# class FoodClassificationDetail(mixins.RetrieveModelMixin,
# 					mixins.UpdateModelMixin,
# 					mixins.DestroyModelMixin,
# 					generics.GenericAPIView):
# 	model = FoodClassification
# 	serializer_class = FoodClassificationSerializers

# 	def get_queryset(self, *args, **kwargs):
# 		return self.model.objects.all()

# 	def get(self, request, *args, **kwargs):
# 		return self.retrieve(request, *args, **kwargs)

# 	def put(self, request, *args, **kwargs):
# 		return self.update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)

# class DisheListPage(mixins.ListModelMixin,
# 					generics.GenericAPIView):
# 	model = Dishes
# 	serializer_class = DishesSerializers
# 	pagination_class = StandardResultsSetPagination

# 	def get_queryset(self, *args, **kwargs):
# 		return self.model.objects.all()

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# class DishesList(mixins.ListModelMixin,
# 				mixins.CreateModelMixin,
# 				generics.GenericAPIView):

# 	model = Dishes
# 	serializer_class = DishesSerializers

# 	def get_queryset(self, *args, **kwargs):
# 		return self.model.objects.all()

# 	def get(self, request, *args, **kwargs):
# 		return self.list(request, *args, **kwargs)

# 	def post(self, request, *args, **kwargs):
# 		return self.create(request, *args, **kwargs)

# class DishesDetail(mixins.RetrieveModelMixin,
# 					mixins.UpdateModelMixin,
# 					mixins.DestroyModelMixin,
# 					generics.GenericAPIView):
# 	model = Dishes
# 	serializer_class = DishesSerializers

# 	def get_queryset(self, *args, **kwargs):
# 		return self.model.objects.all()

# 	def get(self, request, *args, **kwargs):
# 		print(kwargs)
# 		return self.retrieve(request, *args, **kwargs)

# 	def put(self, request, *args, **kwargs):
# 		print(request.data,args,kwargs)
# 		return self.partial_update(request, *args, **kwargs)

# 	def delete(self, request, *args, **kwargs):
# 		return self.destroy(request, *args, **kwargs)