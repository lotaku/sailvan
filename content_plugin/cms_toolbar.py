from cms.extensions.toolbar import ExtensionToolbar
from cms.toolbar_pool import toolbar_pool
from django.utils.translation import ugettext_lazy as _
from .models import TagExtension


@toolbar_pool.register
class IconExtensionToolbar(ExtensionToolbar):
    # defineds the model for the current toolbar
    model = TagExtension

    def populate(self):
        # setup the extension toolbar with permissions and sanity checks
        current_page_menu = self._setup_extension_toolbar()
        # if it's all ok
        if current_page_menu:
            # retrieves the instance of the current extension (if any) and the toolbar item url
            page_extension, url = self.get_page_extension_admin()
            if url:
                # adds a toolbar item
                current_page_menu.add_modal_item(_('Page Extra Attr'), url=url,
                    disabled=not self.toolbar.edit_mode)