# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Country'
        db.create_table('locality_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('iso2', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('iso3', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
        ))
        db.send_create_signal('locality', ['Country'])

        # Adding model 'Territory'
        db.create_table('locality_territory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(related_name='territories', to=orm['locality.Country'])),
        ))
        db.send_create_signal('locality', ['Territory'])


    def backwards(self, orm):
        
        # Deleting model 'Country'
        db.delete_table('locality_country')

        # Deleting model 'Territory'
        db.delete_table('locality_territory')


    models = {
        'locality.country': {
            'Meta': {'ordering': "('iso2', 'name')", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso2': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'iso3': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'})
        },
        'locality.territory': {
            'Meta': {'ordering': "('abbr', 'name')", 'object_name': 'Territory'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'territories'", 'to': "orm['locality.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['locality']
