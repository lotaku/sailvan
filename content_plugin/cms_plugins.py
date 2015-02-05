from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from content_plugin.models import PostBox, IndexContentBox
from django.utils.translation import ugettext as _
import copy
#
# class CMSIndexContentBoxPlugin(CMSPluginBase):
# 	model = IndexContentBoxPlugin3  # model where plugin data are saved
# 	module = _("IndexContentBox")
# 	name = _("IndexContentBox Plugin")  # name of the plugin in the interface
# 	# render_template = "indexbox_plugin.html"
# 	# frontend_edit_template = "indexbox_plugin_edit.html"
# 	_fieldsets = [
# 		(None, {
# 			'fields': ['title', 'url', 'coverImg', 'body', 'small_title', 'img_location', 'background_color']
# 		}),
# 		# (None, {
# 		# 	'fields': ['key_visual', 'lead_in', 'category', 'tags']
# 		# }),
# 		# ('Content', {
# 		# 	'classes': ['plugin-holder', 'plugin-holder-nopage'],
# 		# 	'fields': ['content']
# 		# }),
# 	]
#
# 	def get_fieldsets(self, request, obj=None):
# 		fieldsets = copy.deepcopy(self._fieldsets)
#
# 		return fieldsets
#
#
# 	def render(self, context, instance, placeholder):
# 		context.update({'instance': instance})
# 		return context
#
# 	def get_render_template(self, context, instance, placeholder):
# 		# if instance.attr == '1':
# 		if 1:
# 			return 'indexbox_plugin.html'
# 		else:
# 			return 'template2.html'
#
#
# plugin_pool.register_plugin(CMSIndexContentBoxPlugin)  # register the plugin



class CMSIndexMainBoxPlugin(CMSPluginBase):
	model = IndexContentBox  # model where plugin data are saved
	module = _("IndexContentBox")
	name = _("IndexContentBox")  # name of the plugin in the interface
	# render_template = "indexbox_plugin.html"
	# frontend_edit_template = "indexbox_plugin_edit.html"
	_fieldsets = [
		(None, {
			'fields': ['title', 'url', 'coverImg', 'body', 'small_title', 'img_location', 'background_color']
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
		# if instance.attr == '1':
		if 1:
			return 'indexbox_plugin.html'
		else:
			return 'template2.html'


plugin_pool.register_plugin(CMSIndexMainBoxPlugin)  # register the plugin



class CMSPostBoxPlugin(CMSPluginBase):
	model = PostBox  # model where plugin data are saved
	module = _("IndexContentBox")
	name = _("PostBox")  # name of the plugin in the interface
	# render_template = "indexbox_plugin.html"
	# frontend_edit_template = "indexbox_plugin_edit.html"
	_fieldsets = [
		(None, {
			'fields': ['title', 'template', 'body']
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
		if instance.template == 'common_template':
		# if 1:
			return 'common_template.html'
		else:
			return 'template2.html'


plugin_pool.register_plugin(CMSPostBoxPlugin)  # register the plugin