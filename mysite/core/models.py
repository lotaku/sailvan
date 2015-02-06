# encoding: utf-8

from django.db import models
from datetime import datetime
# import django.contrib.auth.models as django_auth
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
def get_default_user(User):
	return User.objects.get(id=1)
from cms.models.pluginmodel import CMSPlugin

class Object(models.Model):
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

# 用挂件处理
# advantage = models.TextField(blank=True,null=True) #核心优势
# industries = models.TextField(blank=True,null=True) #适用企业
# certifications =  models.TextField(blank=True,null=True) #资质
# award = models.TextField(blank=True,null=True) #公司荣耀


class CObject(CMSPlugin):
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
	order = models.IntegerField(max_length=256, null=True, blank=True)
	tag = models.CharField(max_length=256, blank=True, null=True)



