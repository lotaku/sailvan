# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'IndexContentBoxPlugin'
        db.delete_table(u'content_plugin_indexcontentboxplugin')


    def backwards(self, orm):
        # Adding model 'IndexContentBoxPlugin'
        db.create_table(u'content_plugin_indexcontentboxplugin', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=256, null=True, blank=True)),
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('background_color', self.gf('django.db.models.fields.CharField')(default=1, max_length=256)),
            ('small_title', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'content_plugin', ['IndexContentBoxPlugin'])


    models = {
        
    }

    complete_apps = ['content_plugin']