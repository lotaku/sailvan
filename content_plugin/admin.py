from django.contrib import admin
from .models import IndexContentBoxPlugin3
from .forms import  BoxForm
# Register your models here.

import cms
from cms.admin.placeholderadmin import PlaceholderAdmin, FrontendEditableAdmin


class IndexContentBoxPluginAdmin(FrontendEditableAdmin, PlaceholderAdmin):
	list_display = ['title', ]
	frontend_editable_fields = ('title',)
	# form = BoxForm
	fieldsets = (
		(None, {
			'fields': ('title', 'url', 'body', 'coverImg', 'small_title')
		}),

	)

	def get_fieldsets(self, request, obj=None):
		fieldsets = [
			(None, {'fields': ['url', 'order']}),
		]
		return fieldsets


# class IndexContentBoxinInline(admin.StackedInline):
# 	model = IndexContentBox
# 	extra = 1
#
#
# class IndexContentBoxPluginAdmin(admin.ModelAdmin):
# 	# inlines = [Widget]
# 	model = IndexContentBoxPlugin
# 	# raw_id_fields = ('parent',)
# 	# search_fields = ['parent__title']
# 	search_fields = ['id']
# 	# inlines = [IndexContentBox]
# 	fieldsets = (
# 		(None, {
# 			'fields': ('url', 'order')
# 		}),
#
# 	)
#
admin.site.register(IndexContentBoxPlugin3, IndexContentBoxPluginAdmin)