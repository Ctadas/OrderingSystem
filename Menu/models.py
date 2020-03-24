from django.db import models

# Create your models here.
class FoodClassification(models.Model):
	name = models.Charfield(verbose_name='菜品分类',max_length = 50)

	def __str__ (self):
		return self.name

	class Meta:
		verbose_name = '菜品分类'
		verbose_name_plural = '菜品分类'

class Dishes(models.Model):
	classification = models.ForeignKey('FoodClassification',on_delete=models.CASCADE)
	name = models.Charfield(verbose_name='菜品名称',max_length = 50)
	price = models.FloatField(verbose_name='价格')
	discount_price = models.FloatField(verbose_name='折扣价格',blank = True)
	img = models.ImageField(verbose_name='菜品图片',upload_to='dishes/')
	stock = models.IntegerField(verbose_name='库存',default = 0)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '菜品'
		verbose_name_plural = '菜品'