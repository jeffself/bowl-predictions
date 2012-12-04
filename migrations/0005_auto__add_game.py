# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Game'
        db.create_table('bowls_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bowl', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bowls.Bowl'])),
            ('season', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('game_date', self.gf('django.db.models.fields.DateField')()),
            ('visitor_school', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='visitor_school', null=True, to=orm['bowls.School'])),
            ('visitor_predicted_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('visitor_school_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('home_school', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='home_school', null=True, to=orm['bowls.School'])),
            ('home_school_predicted_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('home_school_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('bowls', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Game'
        db.delete_table('bowls_game')


    models = {
        'bowls.bowl': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Bowl'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'})
        },
        'bowls.conference': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Conference'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'bowls.game': {
            'Meta': {'object_name': 'Game'},
            'bowl': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bowls.Bowl']"}),
            'game_date': ('django.db.models.fields.DateField', [], {}),
            'home_school': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'home_school'", 'null': 'True', 'to': "orm['bowls.School']"}),
            'home_school_predicted_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home_school_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'visitor_predicted_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'visitor_school': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'visitor_school'", 'null': 'True', 'to': "orm['bowls.School']"}),
            'visitor_school_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'bowls.school': {
            'Meta': {'ordering': "('name',)", 'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mascot': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['bowls']