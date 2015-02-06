# -*- coding: UTF-8 –*-
from django.contrib import admin
from .models import  TagExtension
# from .forms import  BoxForm
# Register your models here.
from cms.admin.placeholderadmin import FrontendEditableAdminMixin

from django.contrib import admin
from cms.extensions import PageExtensionAdmin
import cms
from cms.admin.placeholderadmin import PlaceholderAdmin, FrontendEditableAdmin

# 添加 page 的扩展属性到 admin 后台管理


class TagExtensionAdmin(PageExtensionAdmin):
	list_display = ['tag', ]

	def __unicode__(self):
		return u'Tag'

admin.site.register(TagExtension, TagExtensionAdmin)

#
# class IndexContentBoxPluginAdmin(FrontendEditableAdminMixin, admin.ModelAdmin):
# 	list_display = ['title', ]
# 	frontend_editable_fields = ('title', 'body')
#
# 	# form = BoxForm
# 	fieldsets = (
# 		(None, {
# 			'fields': ('title', 'url', 'body', 'coverImg', 'small_title')
# 		}),
#
# 	)
#
# 	def get_fieldsets(self, request, obj=None):
# 		fieldsets = [
# 			(None, {'fields': ['url', 'order']}),
# 		]
# 		return fieldsets
#
#
# admin.site.register(IndexContentBoxPlugin3, IndexContentBoxPluginAdmin)
#
#
# class IndexContentBoxPluginAdmin(FrontendEditableAdmin, PlaceholderAdmin):
# 	list_display = ['title', ]
# 	frontend_editable_fields = ('title',)
# 	# form = BoxForm
# 	fieldsets = (
# 		(None, {
# 			'fields': ('title', 'url', 'body', 'coverImg', 'small_title')
# 		}),
#
# 	)
#
# 	def get_fieldsets(self, request, obj=None):
# 		fieldsets = [
# 			(None, {'fields': ['url', 'order']}),
# 		]
# 		return fieldsets
#
#
# # class IndexContentBoxinInline(admin.StackedInline):
# # 	model = IndexContentBox
# # 	extra = 1
# #
# #
# # class IndexContentBoxPluginAdmin(admin.ModelAdmin):
# # 	# inlines = [Widget]
# # 	model = IndexContentBoxPlugin
# # 	# raw_id_fields = ('parent',)
# # 	# search_fields = ['parent__title']
# # 	search_fields = ['id']
# # 	# inlines = [IndexContentBox]
# # 	fieldsets = (
# # 		(None, {
# # 			'fields': ('url', 'order')
# # 		}),
# #
# # 	)
# #
# admin.site.register(IndexContentBoxPlugin3, IndexContentBoxPluginAdmin)
#
