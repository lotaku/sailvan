# encoding:utf-8
from django.db import models
from mysite.core.models import CObject
from cms.models.pluginmodel import CMSPlugin
from datetime import datetime
from cms.models.fields import PlaceholderField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from ckeditor.fields import RichTextField
# 扩展 page 的属性


class TagExtension(PageExtension):
	tag = models.CharField(max_length=256, blank=True, null=True)
	info_banner = models.ImageField(upload_to='info_banner/%Y%m%d', blank=True, null=True)  # page的图片
	brief = RichTextField(blank=True, null=True)  # page简介

extension_pool.register(TagExtension)


def my_placeholder_slotname(instance):
	return 'boxes'


class IndexContentBox(CObject):
	# index_content_box = models.ForeignKey(IndexContentBox)
	my_placeholder = PlaceholderField(my_placeholder_slotname)

	IMG_LOCATION_CHOICES = [('lpic465', '图片在左边'), ('pic465', '图片在右边')]
	BACKGROUND_COLOR_CHOICES = [(u'#ffffff', u'白色'), (u'#f7f5f8', u'灰色')	]
	#
	url = models.URLField(max_length=256, blank=True, null=True)
	small_title = models.TextField(blank=True, null=True)
	# style
	img_location = models.CharField(max_length=256, choices=IMG_LOCATION_CHOICES, default=1)
	background_color = models.CharField(max_length=256, choices=BACKGROUND_COLOR_CHOICES, default=1)

	def __unicode__(self):
		return self.title


class PostBox(CObject):
	# index_content_box = models.ForeignKey(IndexContentBox)

	def __unicode__(self):
		return self.title

	TEMPLATE_CHOICES = [
		(u"common_template", u'常规'),
		(u'list_04_template', u'列表4'),
		(u'body_stowable', u'可隐藏部分内容'),
		(u'tabs_01_template', u'显示某tag的文章'),
		(u'show_sub_page_in_post', u'显示_指定_页面的子页面简介'),
		(u'show_current_page_sub_page_brief', u'显示_当前_页面子页面简介')
	]
	reverse_id = models.CharField(max_length=256, blank=True, null=True)
	show_dividing_line = models.NullBooleanField(default=2, blank=True, null=True)
	template = models.CharField(max_length=256, choices=TEMPLATE_CHOICES, default=1)


class RightBox(CObject):
	TEMPLATE_CHOICES = [(u'right_box_common', u'常规')	]
	template = models.CharField(max_length=256, choices=TEMPLATE_CHOICES, default=1)

	def __unicode__(self):
		return self.title


class IndexShowBox(CObject):
	TEMPLATE_CHOICES = [(u'index_show_box_common', u'常规')	]
	template = models.CharField(max_length=256, choices=TEMPLATE_CHOICES, default=1)
	title_url = models.URLField(max_length=256, blank=True, null=True)
	body_url = models.URLField(max_length=256, blank=True, null=True)
	# style
	css_top = models.CharField(max_length=256, blank=True, null=True)
	css_left = models.CharField(max_length=256, blank=True, null=True)

	def __unicode__(self):
		return self.title


class Menu_1(CObject):
	TEMPLATE_CHOICES = [(u'menu_1', u'常规'), (u'menu_2', u'带图列表')	]
	template = models.CharField(max_length=256, choices=TEMPLATE_CHOICES, default=1)
	title_url = models.URLField(max_length=256, blank=True, null=True)
	body_url = models.URLField(max_length=256, blank=True, null=True)
	reverse_id = models.CharField(max_length=256)
	# style

	def __unicode__(self):
		return self.title

# class Post(CObject):
# 	TEMPLATE_CHOICES = [(u'menu_show_sub_page_in_post', u'在主内容区显示子页面简介')	]
# 	template = models.CharField(max_length=256, choices=TEMPLATE_CHOICES, default=1)
# 	title_url = models.URLField(max_length=256, blank=True, null=True)
# 	body_url = models.URLField(max_length=256, blank=True, null=True)
# 	reverse_id = models.CharField(max_length=256)
# 	# style
#
# 	def __unicode__(self):
# 		return self.reverse_id


#以下是测试的
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
