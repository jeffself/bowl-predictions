# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'School', fields ['name']
        db.create_unique('bowls_school', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'School', fields ['name']
        db.delete_unique('bowls_school', ['name'])


    models = {
        'bowls.school': {
            'Meta': {'ordering': "('name',)", 'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mascot': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['bowls']