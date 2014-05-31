# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'core_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'core', ['Address'])

        # Adding model 'Outlet'
        db.create_table(u'core_outlet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django_extensions.db.fields.AutoSlugField')(allow_duplicates=False, max_length=50, separator=u'-', blank=True, unique=True, populate_from='name', overwrite=False)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(related_name='address', to=orm['core.Address'])),
            ('position', self.gf('geoposition.fields.GeopositionField')(max_length=42)),
        ))
        db.send_create_signal(u'core', ['Outlet'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'core_address')

        # Deleting model 'Outlet'
        db.delete_table(u'core_outlet')


    models = {
        u'core.address': {
            'Meta': {'object_name': 'Address'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'core.outlet': {
            'Meta': {'ordering': "('-modified', '-created')", 'object_name': 'Outlet'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'address'", 'to': u"orm['core.Address']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'position': ('geoposition.fields.GeopositionField', [], {'max_length': '42'}),
            'slug': ('django_extensions.db.fields.AutoSlugField', [], {'allow_duplicates': 'False', 'max_length': '50', 'separator': "u'-'", 'blank': 'True', 'unique': 'True', 'populate_from': "'name'", 'overwrite': 'False'})
        }
    }

    complete_apps = ['core']