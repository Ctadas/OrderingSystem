from django.shortcuts import render
from Menu.models import Dishes,FoodClassification
from django.shortcuts import render
from Menu.serializers import DishesSerializers,FoodClassificationSerializers,StandardResultsSetPagination
from rest_framework import mixins,generics,viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt import authentication as jwt_authentication
from rest_framework.response import Response

from PersonnelManagement.models import Personnel
from rest_framework import permissions


def dishes_management(request):
	return render(request, 'menu/index.html')


class FoodClassificationViewSet(viewsets.ModelViewSet):
	queryset = FoodClassification.objects.all()
	serializer_class = FoodClassificationSerializers 

	authentication_classes = [SessionAuthentication, BasicAuthentication,jwt_authentication.JWTAuthentication]
	permission_classes = [IsAuthenticated]


class WXPermission(permissions.BasePermission):
	"""
	Global permission check for blacklisted IPs.
	"""
	def has_permission(self, request, view):
		return True
		
class TestJWTAuthentication(jwt_authentication.JWTAuthentication):
	def get_user(self, validated_token):
		"""
		Attempts to find and return a user using the given validated token.
		"""
		try:
			user_id = validated_token[jwt_authentication.api_settings.USER_ID_CLAIM]
		except KeyError:
			raise InvalidToken(_('Token contained no recognizable user identification'))
		try:
			user = Personnel.objects.get(**{jwt_authentication.api_settings.USER_ID_FIELD: user_id})
		except Personnel.DoesNotExist:
			raise AuthenticationFailed(_('User not found'), code='user_not_found')

		return user

class DishesViewSet(viewsets.ModelViewSet):
	queryset = Dishes.objects.all()
	serializer_class = DishesSerializers 
	authentication_classes = [SessionAuthentication, BasicAuthentication,TestJWTAuthentication]
	permission_classes = [WXPermission]

class DishesPageViewSet(viewsets.ModelViewSet):
	queryset = Dishes.objects.all()
	serializer_class = DishesSerializers 
	pagination_class = StandardResultsSetPagination

	authentication_classes = [SessionAuthentication, BasicAuthentication,TestJWTAuthentication]
	permission_classes = [WXPermission]
