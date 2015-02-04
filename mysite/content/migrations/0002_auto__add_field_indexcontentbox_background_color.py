# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'IndexContentBox.background_color'
        db.add_column(u'content_indexcontentbox', 'background_color',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=256),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'IndexContentBox.background_color'
        db.delete_column(u'content_indexcontentbox', 'background_color')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'content.article': {
            'Meta': {'object_name': 'Article', '_ormbases': [u'core.Object']},
            'common_widget': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'articles'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['content.CommonWidget']"}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sup_page'", 'null': 'True', 'to': u"orm['content.Article']"})
        },
        u'content.commonwidget': {
            'Meta': {'object_name': 'CommonWidget', '_ormbases': [u'core.Object']},
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'content.footerbox': {
            'Meta': {'object_name': 'FooterBox', '_ormbases': [u'core.Object']},
            'body_1': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'body_2': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'img_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'img_2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'content.indexcontentbox': {
            'Meta': {'object_name': 'IndexContentBox', '_ormbases': [u'core.Object']},
            'background_color': ('django.db.models.fields.CharField', [], {'default': '1', 'max_length': '256'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'small_title': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'content.indexshowcase': {
            'Meta': {'object_name': 'IndexShowcase', '_ormbases': [u'core.Object']},
            'body_url': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'css_left': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'css_top': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'title_url': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'content.new': {
            'Meta': {'object_name': 'New', '_ormbases': [u'core.Object']},
            u'object_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['core.Object']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'content.widget': {
            'Meta': {'object_name': 'Widget'},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['content.Article']", 'null': 'True'}),
            'body': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.object': {
            'Meta': {'object_name': 'Object'},
            'bannerImg': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'body': ('ckeditor.fields.RichTextField', [], {'null': 'True', 'blank': 'True'}),
            'brief': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'coverImg': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cretor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'menu_level': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '256', 'null': 'True'}),
            'menu_order': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '256', 'null': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'max_length': '256', 'null': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type_first': ('django.db.models.fields.IntegerField', [], {'default': '1', 'max_length': '256'})
        }
    }

    complete_apps = ['content']