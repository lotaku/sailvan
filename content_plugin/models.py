from django.db import models
from cms.models import CMSPlugin
from mysite.content.models import IndexContentBox


class IndexContentBoxPlugin(CMSPlugin):
    index_content_box = models.ForeignKey(IndexContentBox)

    def copy_relations(self, oldinstance):
        for associated_item in oldinstance.index_content_box2.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            associated_item.pk = None
            associated_item.plugin = self
            associated_item.save()

    def __unicode__(self):
        return self.index_content_box.title

class AssociatedItem(models.Model):
    index_content_box2 = models.ForeignKey(
        IndexContentBoxPlugin,
        related_name="index_content_box2"
        )
