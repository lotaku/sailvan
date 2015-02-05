# encoding:utf-8
from django.db import models

from cms.models.pluginmodel import CMSPlugin
from datetime import datetime
from cms.models.fields import PlaceholderField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

def my_placeholder_slotname(instance):
	return 'boxes'

class CMSObject(CMSPlugin):
	"Generic wwhf object"
	TYPE_CHOICES = [
		(1, '专业服务'),
		(2, '技术服务'),
		(3, '新业务'),
		(4, '关于万维合丰'),
		(5, '加入我们'),
		(6, '备用1'),
		(7, '备用2'),
		(8, '备用3'),
	]
	cretor = models.ForeignKey(User, null=True, blank=True)
	last_updated = models.DateTimeField(auto_now=True)
	date_created = models.DateTimeField(default=datetime.now)

	title = models.TextField(blank=True, null=True)
	# body = models.TextField(blank=True,null=True)
	body = RichTextField(blank=True, null=True)
	brief = models.TextField(blank=True, null=True)  # 简介

	bannerImg = models.ImageField(upload_to='bannerImg/%Y%m%d', blank=True, null=True)  # 标题后面的背景图
	type_first = models.IntegerField(max_length=256, choices=TYPE_CHOICES, default=1)
	menu_order = models.IntegerField(max_length=256, default=1, null=True)
	menu_level = models.IntegerField(max_length=256, default=1, null=True)
	coverImg = models.ImageField(upload_to='coverImg/%Y%m%d', blank=True, null=True)
	order = models.IntegerField(max_length=256, null=True)

class IndexContentBoxPlugin3(CMSObject):
	# index_content_box = models.ForeignKey(IndexContentBox)
	my_placeholder = PlaceholderField(my_placeholder_slotname)

	IMG_LOCATION_CHOICES = [('lpic465', '图片在左边'), ('pic465', '图片在右边')		]
	BACKGROUND_COLOR_CHOICES = [(u'#ffffff', u'白色'), (u'#f7f5f8', u'灰色')		]
	#
	url = models.URLField(max_length=256, blank=True, null=True)
	small_title = models.TextField(blank=True, null=True)
	# style
	img_location = models.CharField(max_length=256, choices=IMG_LOCATION_CHOICES, default=1)
	background_color = models.CharField(max_length=256, choices=BACKGROUND_COLOR_CHOICES, default=1)

	def __unicode__(self):
		return self.title
		# return 'box pluginxx'
#
# class IndexContentBoxPlugin(CMSPlugin, CMSObject):
# 	# index_content_box = models.ForeignKey(IndexContentBox)
# 	# my_placeholder = PlaceholderField(my_placeholder_slotname)
#
# 	BACKGROUND_COLOR_CHOICES = [(u'#ffffff', u'白色'), (u'#f7f5f8', u'灰色')		]
#
# 	url = models.URLField(max_length=256, blank=True, null=True)
# 	small_title = models.TextField(blank=True, null=True)
# 	# style
# 	# img_location = models.CharField(max_length=256, choices=IMG_LOCATION_CHOICES, default=1)
# 	background_color = models.CharField(max_length=256, choices=BACKGROUND_COLOR_CHOICES, default=1)
#
# 	def __unicode__(self):
# 		return self.small_title

	# def copy_relations(self, oldinstance):
		# for associated_item in oldinstance.index_content_box2.all():
		# 	# instance.pk = None; instance.pk.save() is the slightly odd but
		# 	# standard Django way of copying a saved model instance
		# 	associated_item.pk = None
		# 	associated_item.plugin = self
		# 	associated_item.save()

# #
# class AssociatedItem(models.Model):
# 	index_content_box2 = models.ForeignKey(
# 		IndexContentBoxPlugin,
# 		related_name="index_content_box2")



#
# class MyModel(models.Model):
#     # your fields
#     my_placeholder = PlaceholderField(my_placeholder_slotname)
#     # your methods