from django.db import models

# Create your models here.

# 微信用户模型
class Personnel(models.Model):
	open_id =  models.CharField(verbose_name='微信唯一识别码',max_length = 50)
	session_key = models.CharField(verbose_name='会话秘钥',max_length=50)
	address_management = models.ManyToManyField('Address',verbose_name='地址管理')

	def __str__(self):
		return self.open_id

	class Meta:
		verbose_name = '微信用户管理'
		verbose_name_plural = '微信用户管理'

# 地址管理
class Address(models.Model):
	consignee = models.CharField(verbose_name='收货人',max_length=50)
	phone = models.BigIntegerField(verbose_name='收货电话')
	dom = models.CharField(verbose_name='收货地址',max_length=50)
	
	def __str__(self):
		return self.consignee

	class Meta:
		verbose_name = '地址管理'
		verbose_name_plural = '地址管理'
