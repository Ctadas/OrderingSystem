from django.db import models
from django.db.models.signals import post_init,post_save,post_delete
from django.dispatch import receiver
from lxml import etree
from django.conf import settings
import os

# Create your models here.
# 菜品分类模型
class FoodClassification(models.Model):
	name = models.CharField(verbose_name='菜品分类',max_length = 50)

	def __str__ (self):
		return self.name

	class Meta:
		verbose_name = '菜品分类'
		verbose_name_plural = '菜品分类'

# 菜品模型
class Dishes(models.Model):
	classification = models.ForeignKey('FoodClassification',on_delete=models.CASCADE)
	name = models.CharField(verbose_name='菜品名称',max_length = 50)
	price = models.FloatField(verbose_name='价格')
	discount_price = models.FloatField(verbose_name='折扣价格',blank = True)
	img = models.ImageField(verbose_name='菜品图片',upload_to='dishes/')
	shelves_status = models.BooleanField(verbose_name='是否上架',default=True)
	stock = models.IntegerField(verbose_name='库存',default = 0)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '菜品'
		verbose_name_plural = '菜品'

# 菜品模型初始化信号
@receiver(post_init, sender=Dishes)
def img_init(sender,instance,**kwargs):
	instance._bak_img = instance.img

# 菜品模型保存信号
@receiver(post_save, sender=Dishes)
def img_change(sender,instance,**kwargs):
	if instance._bak_img:
		if instance.img != instance._bak_img:
			file_url = os.path.join(settings.MEDIA_ROOT, str(instance._bak_img))
			if os.path.isfile(file_url):
				os.remove(file_url)
				del_empty_dir(settings.MEDIA_ROOT)

# 菜品模型删除信号
@receiver(post_delete, sender=Dishes)
def delete_upload_files(sender, instance, **kwargs):
	del_url = []
	file_url = os.path.join(settings.MEDIA_ROOT, str(instance.img))	
	# content_html = etree.HTML(instance.content)
	# content_img_src = content_html.xpath('//img/@src')
	# for img_src in content_img_src:
	# 	img_src = os.path.join(settings.BASE_DIR, img_src[1:])
	# 	del_url.append(os.path.join(settings.BASE_DIR, img_src).replace('\\','/'))
	del_url.append(file_url.replace('\\','/'))
	for durl in del_url:
		if os.path.isfile(durl):
			os.remove(durl)

	del_empty_dir(settings.MEDIA_ROOT)

# 删除空的文件夹
def del_empty_dir(dir):
	if os.path.isdir(dir):
		for item in os.listdir(dir):
			del_empty_dir(os.path.join(dir,item))

		if not os.listdir(dir):
			os.rmdir(dir)