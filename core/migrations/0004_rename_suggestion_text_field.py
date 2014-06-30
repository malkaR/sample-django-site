# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for record in orm.GoogleSuggestion.objects.all():
            record.search_text = record.suggestions
            record.save()

    def backwards(self, orm):
        raise RuntimeError("Cannot reverse this migration.")

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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.googlequery': {
            'Meta': {'object_name': 'GoogleQuery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query_terms': ('django.db.models.fields.TextField', [], {})
        },
        u'core.googlesuggestion': {
            'Meta': {'object_name': 'GoogleSuggestion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'search_text': ('django.db.models.fields.TextField', [], {}),
            'suggestions': ('django.db.models.fields.TextField', [], {})
        },
        u'core.usergooglequery': {
            'Meta': {'object_name': 'UserGoogleQuery'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'google_query': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'google_query_set'", 'to': u"orm['core.GoogleQuery']"}),
            'humorous_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspiration_item': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.UserGoogleQuery']", 'null': 'True'}),
            'inspiration_query': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'inspiration_query_set'", 'null': 'True', 'to': u"orm['core.GoogleQuery']"}),
            'meaning_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'suggestions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.GoogleSuggestion']", 'through': u"orm['core.UserQuerySuggestion']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'core.userquerysuggestion': {
            'Meta': {'object_name': 'UserQuerySuggestion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'suggestion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.GoogleSuggestion']"}),
            'user_query': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.UserGoogleQuery']"})
        }
    }

    complete_apps = ['core']
    symmetrical = True
