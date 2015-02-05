# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'IndexContentBoxPlugin.index_content_box'
        db.delete_column(u'content_plugin_indexcontentboxplugin', 'index_content_box_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'IndexContentBoxPlugin.index_content_box'
        raise RuntimeError("Cannot reverse this migration. 'IndexContentBoxPlugin.index_content_box' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'IndexContentBoxPlugin.index_content_box'
        db.add_column(u'content_plugin_indexcontentboxplugin', 'index_content_box',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['content.IndexContentBox']),
                      keep_default=False)


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
        u'content_plugin.associateditem': {
            'Meta': {'object_name': 'AssociatedItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index_content_box2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'index_content_box2'", 'to': u"orm['content_plugin.IndexContentBoxPlugin']"})
        },
        u'content_plugin.indexcontentboxplugin': {
            'Meta': {'object_name': 'IndexContentBoxPlugin', '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'my_placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'})
        }
    }

    complete_apps = ['content_plugin']