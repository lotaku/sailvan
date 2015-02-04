from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from content_plugin.models import IndexContentBoxPlugin
from django.utils.translation import ugettext as _


class CMSIndexContentBoxPlugin(CMSPluginBase):
    model = IndexContentBoxPlugin  # model where plugin data are saved
    module = _("IndexContentBox")
    name = _("IndexContentBox Plugin")  # name of the plugin in the interface
    render_template = "indexbox_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(CMSIndexContentBoxPlugin)  # register the plugin