# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Territory.name'
        db.alter_column('locality_territory', 'name', self.gf('django.db.models.fields.CharField')(max_length=64))

        # Changing field 'Country.name'
        db.alter_column('locality_country', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=64))


    def backwards(self, orm):
        
        # Changing field 'Territory.name'
        db.alter_column('locality_territory', 'name', self.gf('django.db.models.fields.CharField')(max_length=32))

        # Changing field 'Country.name'
        db.alter_column('locality_country', 'name', self.gf('django.db.models.fields.CharField')(max_length=32, unique=True))


    models = {
        'locality.country': {
            'Meta': {'ordering': "('iso2', 'name')", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso2': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'iso3': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'locality.territory': {
            'Meta': {'ordering': "('abbr', 'name')", 'object_name': 'Territory'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'territories'", 'to': "orm['locality.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['locality']
