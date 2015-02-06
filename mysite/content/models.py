# encoding: utf-8
from django.db import models
from mysite.core.models import Object
from ckeditor.fields import RichTextField
import random
import os
# Create your models here.
from mysite.settings import PROJECT_ROOT


class CommonWidget(Object):
	def __unicode__(self):
		# screen_name = u'常用挂件'
		return self.title

	# return u'guajian'


class Article(Object):
	parent = models.ForeignKey("self", blank=True, related_name="sup_page", null=True)
	common_widget = models.ManyToManyField(CommonWidget, blank=True, null=True, related_name='articles')

	def get_range_bannerImg(self):
		bannerImg_dir = os.path.join(PROJECT_ROOT, 'static/wwhf_ui/banners')
		bannerImg_name = random.choice(os.listdir(bannerImg_dir))
		bannerImg_path = os.path.join('wwhf_ui/banners', bannerImg_name)
		return bannerImg_path

	def get_range_coverImg(self):
		bannerImg_dir = os.path.join(PROJECT_ROOT, 'static/wwhf_ui/coverimgs')
		bannerImg_name = random.choice(os.listdir(bannerImg_dir))
		bannerImg_path = os.path.join('wwhf_ui/coverimgs', bannerImg_name)
		return bannerImg_path

	def __unicode__(self):
		# self.get_range_bannerImg()
		return self.title

	def get_subpage(self):
		articles = Article.objects.get(self.pk).subpage.all()
		return articles


class Widget(models.Model):
	title = models.CharField(max_length=256, blank=True, null=True)
	body = RichTextField(blank=True, null=True)
	article = models.ForeignKey(Article, null=True)


class New(Object):
	url = models.URLField(max_length=256, blank=True, null=True)

	def __unicode__(self):
		return self.title


class IndexShowcase(Object):
	title_url = models.URLField(max_length=256, blank=True, null=True)
	body_url = models.URLField(max_length=256, blank=True, null=True)

	# style
	css_top = models.CharField(max_length=256, blank=True, null=True)
	css_left = models.CharField(max_length=256, blank=True, null=True)

	def __unicode__(self):
		return self.title


class IndexContentBox(Object):
	# IMG_LOCATION_CHOICES = [('lpic465', '图片在左边'), ('lpic465', '图片在右边')		]
	BACKGROUND_COLOR_CHOICES = [(u'#ffffff', u'白色'), (u'#f7f5f8', u'灰色')		]

	url = models.URLField(max_length=256, blank=True, null=True)
	small_title = models.TextField(blank=True, null=True)

	# style
	# img_location = models.CharField(max_length=256, choices=IMG_LOCATION_CHOICES, default=1)
	background_color = models.CharField(max_length=256, choices=BACKGROUND_COLOR_CHOICES, default=1)



	def __unicode__(self):
		return self.title


class FooterBox(Object):

	# url = models.URLField(max_length=256, blank=True, null=True)
	img_1 = models.ImageField(upload_to='FooterImg/', blank=True, null=True)
	body_1 = RichTextField(blank=True, null=True)

	img_2 = models.ImageField(upload_to='FooterImg/', blank=True, null=True)
	body_2 = RichTextField(blank=True, null=True)

	def __unicode__(self):
		return self.title