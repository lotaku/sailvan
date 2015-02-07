from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from content_plugin.models import PostBox, IndexContentBox, RightBox, IndexShowBox, Menu_1
from django.utils.translation import ugettext as _
import copy

class CMSIndexMainBoxPlugin(CMSPluginBase):
	model = IndexContentBox  # model where plugin data are saved
	module = _("Boxes")
	name = _("IndexContentBox")  # name of the plugin in the interface
	# render_template = "indexbox_plugin.html"
	# frontend_edit_template = "indexbox_plugin_edit.html"
	_fieldsets = [(None, {'fields': ['title', 'url', 'coverImg', 'body', 'small_title', 'img_location', 'background_color']}),	]

	def get_fieldsets(self, request, obj=None):
		fieldsets = copy.deepcopy(self._fieldsets)

		return fieldsets


	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context

	def get_render_template(self, context, instance, placeholder):
		# if instance.attr == '1':
		if 1:
			return 'indexbox_plugin.html'
		else:
			return 'template2.html'


plugin_pool.register_plugin(CMSIndexMainBoxPlugin)  # register the plugin


class CMSPostBoxPlugin(CMSPluginBase):
	model = PostBox  # model where plugin data are saved
	module = _("Boxes")
	name = _("PostBox")  # name of the plugin in the interface
	# render_template = "indexbox_plugin.html"
	# frontend_edit_template = "indexbox_plugin_edit.html"
	_fieldsets = [
		(None, {
			'fields': ['template', 'title', 'body', 'coverImg', 'tag', 'reverse_id']
		}),
		# (None, {
		# 	'fields': ['key_visual', 'lead_in', 'category', 'tags']
		# }),
		# ('Content', {
		# 	'classes': ['plugin-holder', 'plugin-holder-nopage'],
		# 	'fields': ['content']
		# }),
	]

	def get_fieldsets(self, request, obj=None):
		fieldsets = copy.deepcopy(self._fieldsets)

		return fieldsets

	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context

	def get_render_template(self, context, instance, placeholder):
		return instance.template + '.html'

plugin_pool.register_plugin(CMSPostBoxPlugin)  # register the plugin


class CMSRightBoxPlugin(CMSPluginBase):
	model = RightBox
	module = _("Boxes")
	name = _("RightBox")
	_fieldsets = [
		(None, {
			'fields': ['title', 'template', 'coverImg', 'tag']
		})]

	def get_fieldsets(self, request, obj=None):
		fieldsets = copy.deepcopy(self._fieldsets)

		return fieldsets


	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context

	def get_render_template(self, context, instance, placeholder):
		if instance.template == 'right_box_common':
			return 'right_box_common.html'

plugin_pool.register_plugin(CMSRightBoxPlugin)  # register the plugin


class CMSIndexShowBoxPlugin(CMSPluginBase):
	model = IndexShowBox
	module = _("Boxes")
	name = _("IndexShowBox")
	_fieldsets = [
		(None, {
			'fields': ['title', 'title_url', 'body', 'body_url', 'template', 'css_top', 'css_left', 'coverImg']
		})]

	def get_fieldsets(self, request, obj=None):
		fieldsets = copy.deepcopy(self._fieldsets)

		return fieldsets

	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context

	def get_render_template(self, context, instance, placeholder):
		if instance.template == 'index_show_box_common':
			return 'index_show_box_common.html'

plugin_pool.register_plugin(CMSIndexShowBoxPlugin)  # register the plugin


class CMSMenu_1_Plugin(CMSPluginBase):
	model = Menu_1
	module = _("Menu")
	name = _("Menu_1")
	_fieldsets = [
		(None, {
			'fields': ['template', 'reverse_id']
		})]

	def get_fieldsets(self, request, obj=None):
		fieldsets = copy.deepcopy(self._fieldsets)

		return fieldsets

	def render(self, context, instance, placeholder):
		context.update({'instance': instance})
		return context

	def get_render_template(self, context, instance, placeholder):
		if instance.template == 'menu_1':
			return 'menu_1.html'

plugin_pool.register_plugin(CMSMenu_1_Plugin)  # register the plugin