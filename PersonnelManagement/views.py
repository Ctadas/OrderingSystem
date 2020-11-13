from django.shortcuts import render
from PersonnelManagement.models import Personnel,Address
from PersonnelManagement.serializers import PersonnelSerializers,AddressSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins,generics,viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework_simplejwt import authentication as jwt_authentication
from rest_framework_simplejwt.tokens import RefreshToken
import requests as httprequests
import json 

from PersonnelManagement.models import Personnel
from rest_framework import permissions
# Create your views here.
@api_view(['POST'])
def weixin_login(request):
	url ='https://api.weixin.qq.com/sns/jscode2session'
	code = json.loads(request.body.decode()).get('code')
	appid = ''
	secret = ''
	params = {
		'appid':appid,
		'secret':secret,
		'js_code':code,
		'grant_type':'authorization_code'
	}
	return_request = httprequests.get(url,params)

	print(return_request.json())
	openid = return_request.json()['openid']
	session_key = return_request.json()['session_key']

	personnel, created = Personnel.objects.get_or_create(
		open_id=openid,
		defaults={'session_key': session_key},
	)
	
	refresh = RefreshToken.for_user(personnel)

	return Response({
		'refresh': str(refresh),
		'access': str(refresh.access_token),
	})

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

class PersonnelViewSet(viewsets.ModelViewSet):
	queryset = Personnel.objects.all()
	serializer_class = PersonnelSerializers 

	authentication_classes = [SessionAuthentication, BasicAuthentication,TestJWTAuthentication]
	permission_classes = [WXPermission]

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		serializer = self.get_serializer(instance)
		return Response(serializer.data)
