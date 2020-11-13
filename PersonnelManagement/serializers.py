from rest_framework import serializers
from PersonnelManagement.models import Personnel,Address
from rest_framework.pagination import PageNumberPagination

class PersonnelSerializers(serializers.ModelSerializer):
	class Meta:
		model = Personnel
		fields = '__all__'	


class AddressSerializers(serializers.ModelSerializer):

	class Meta:
		model = Address
		fields = '__all__'	


