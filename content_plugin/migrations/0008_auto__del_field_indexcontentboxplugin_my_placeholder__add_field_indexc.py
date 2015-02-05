# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'IndexContentBoxPlugin.my_placeholder'
        db.delete_column(u'content_plugin_indexcontentboxplugin', 'my_placeholder_id')

        # Adding field 'IndexContentBoxPlugin.url'
        db.add_column(u'content_plugin_indexcontentboxplugin', 'url',
                      self.gf('django.db.models.fields.URLField')(max_length=256, null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexContentBoxPlugin.small_title'
        db.add_column(u'content_plugin_indexcontentboxplugin', 'small_title',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'IndexContentBoxPlugin.background_color'
        db.add_column(u'content_plugin_indexcontentboxplugin', 'background_color',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'IndexContentBoxPlugin.my_placeholder'
        db.add_column(u'content_plugin_indexcontentboxplugin', 'my_placeholder',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True),
                      keep_default=False)

        # Deleting field 'IndexContentBoxPlugin.url'
        db.delete_column(u'content_plugin_indexcontentboxplugin', 'url')

        # Deleting field 'IndexContentBoxPlugin.small_title'
        db.delete_column(u'content_plugin_indexcontentboxplugin', 'small_title')

        # Deleting field 'IndexContentBoxPlugin.background_color'
        db.delete_column(u'content_plugin_indexcontentboxplugin', 'background_color')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'content_plugin.indexcontentboxplugin': {
            'Meta': {'object_name': 'IndexContentBoxPlugin', '_ormbases': ['cms.CMSPlugin']},
            'background_color': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '256'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'small_title': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['content_plugin']