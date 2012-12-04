# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'School.offense_rating'
        db.add_column('bowls_school', 'offense_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'School.defense_rating'
        db.add_column('bowls_school', 'defense_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3, blank=True),
                      keep_default=False)

        # Adding field 'School.games_against_fbs'
        db.add_column('bowls_school', 'games_against_fbs',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.pf_against_fbs'
        db.add_column('bowls_school', 'pf_against_fbs',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.pa_against_fbs'
        db.add_column('bowls_school', 'pa_against_fbs',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.wins'
        db.add_column('bowls_school', 'wins',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.losses'
        db.add_column('bowls_school', 'losses',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'School.power_rating'
        db.add_column('bowls_school', 'power_rating',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'School.offense_rating'
        db.delete_column('bowls_school', 'offense_rating')

        # Deleting field 'School.defense_rating'
        db.delete_column('bowls_school', 'defense_rating')

        # Deleting field 'School.games_against_fbs'
        db.delete_column('bowls_school', 'games_against_fbs')

        # Deleting field 'School.pf_against_fbs'
        db.delete_column('bowls_school', 'pf_against_fbs')

        # Deleting field 'School.pa_against_fbs'
        db.delete_column('bowls_school', 'pa_against_fbs')

        # Deleting field 'School.wins'
        db.delete_column('bowls_school', 'wins')

        # Deleting field 'School.losses'
        db.delete_column('bowls_school', 'losses')

        # Deleting field 'School.power_rating'
        db.delete_column('bowls_school', 'power_rating')


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
            'visitor_school': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'visitor_school'", 'null': 'True', 'to': "orm['bowls.School']"}),
            'visitor_school_predicted_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'visitor_school_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'bowls.school': {
            'Meta': {'ordering': "('name',)", 'object_name': 'School'},
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['bowls.Conference']"}),
            'defense_rating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'games_against_fbs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mascot': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'offense_rating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'pa_against_fbs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pf_against_fbs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'power_rating': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['bowls']