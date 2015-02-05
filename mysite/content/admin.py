# encoding: utf-8
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import Article, Widget, New, IndexShowcase, CommonWidget, IndexContentBox, FooterBox

admin.site.register(Widget)


class WidgetInline(admin.StackedInline):
	model = Widget
	extra = 1


class ArticleAdmin(admin.ModelAdmin):
	# inlines = [Widget]

	raw_id_fields = ('parent',)
	# search_fields = ['parent__title']
	search_fields = ['id']
	inlines = [WidgetInline]


admin.site.register(Article, ArticleAdmin)


class NewAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('url', 'title')
		}),

	)


admin.site.register(New, NewAdmin)


class IndexShowcaseAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('title', 'title_url', 'body', 'body_url', 'coverImg', 'order', 'css_top', 'css_left')
		}),

	)


admin.site.register(IndexShowcase, IndexShowcaseAdmin)


class CommonWidgetAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('title', 'body')
		}),

	)

	def __unicode__(self):
		screen_name = u'常用挂件'
		return screen_name


admin.site.register(CommonWidget, CommonWidgetAdmin)


class IndexContentBoxAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('title', 'small_title', 'url', 'body', 'coverImg' )
		}),

	)


# admin.site.register(IndexContentBox, IndexContentBoxAdmin)



class FooterBoxAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('order', 'title', 'img_1', 'body_1', 'img_2', 'body_2')
		}),

	)

admin.site.register(FooterBox, FooterBoxAdmin)