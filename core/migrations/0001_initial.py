# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GoogleQuery'
        db.create_table(u'core_googlequery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('query_terms', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['GoogleQuery'])

        # Adding model 'GoogleSuggestion'
        db.create_table(u'core_googlesuggestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('suggestions', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'core', ['GoogleSuggestion'])

        # Adding model 'UserGoogleQuery'
        db.create_table(u'core_usergooglequery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('google_query', self.gf('django.db.models.fields.related.ForeignKey')(related_name='google_query_set', to=orm['core.GoogleQuery'])),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('inspiration_query', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='inspiration_query_set', null=True, to=orm['core.GoogleQuery'])),
            ('inspiration_item', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['core.UserGoogleQuery'], null=True)),
            ('meaning_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('humurous_comment', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'core', ['UserGoogleQuery'])

        # Adding model 'UserQuerySuggestion'
        db.create_table(u'core_userquerysuggestion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_query', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.UserGoogleQuery'])),
            ('suggestion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.GoogleSuggestion'])),
            ('rank', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'core', ['UserQuerySuggestion'])


    def backwards(self, orm):
        # Deleting model 'GoogleQuery'
        db.delete_table(u'core_googlequery')

        # Deleting model 'GoogleSuggestion'
        db.delete_table(u'core_googlesuggestion')

        # Deleting model 'UserGoogleQuery'
        db.delete_table(u'core_usergooglequery')

        # Deleting model 'UserQuerySuggestion'
        db.delete_table(u'core_userquerysuggestion')


    models = {
        u'core.googlequery': {
            'Meta': {'object_name': 'GoogleQuery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'query_terms': ('django.db.models.fields.TextField', [], {})
        },
        u'core.googlesuggestion': {
            'Meta': {'object_name': 'GoogleSuggestion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'suggestions': ('django.db.models.fields.TextField', [], {})
        },
        u'core.usergooglequery': {
            'Meta': {'object_name': 'UserGoogleQuery'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'google_query': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'google_query_set'", 'to': u"orm['core.GoogleQuery']"}),
            'humurous_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspiration_item': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['core.UserGoogleQuery']", 'null': 'True'}),
            'inspiration_query': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'inspiration_query_set'", 'null': 'True', 'to': u"orm['core.GoogleQuery']"}),
            'meaning_comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'suggestions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.GoogleSuggestion']", 'through': u"orm['core.UserQuerySuggestion']", 'symmetrical': 'False'})
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