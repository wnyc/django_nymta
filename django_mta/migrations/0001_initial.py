# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TurnstileDownloadComplete'
        db.create_table(u'django_mta_turnstiledownloadcomplete', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'django_mta', ['TurnstileDownloadComplete'])

        # Adding model 'Turnstile'
        db.create_table(u'django_mta_turnstile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('control_area', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('scp', self.gf('django.db.models.fields.CharField')(max_length=8)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('entries_counter', self.gf('django.db.models.fields.BigIntegerField')()),
            ('exits_counter', self.gf('django.db.models.fields.BigIntegerField')()),
            ('entries', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('exits', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'django_mta', ['Turnstile'])


    def backwards(self, orm):
        # Deleting model 'TurnstileDownloadComplete'
        db.delete_table(u'django_mta_turnstiledownloadcomplete')

        # Deleting model 'Turnstile'
        db.delete_table(u'django_mta_turnstile')


    models = {
        u'django_mta.turnstile': {
            'Meta': {'object_name': 'Turnstile'},
            'control_area': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'entries': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'entries_counter': ('django.db.models.fields.BigIntegerField', [], {}),
            'exits': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'exits_counter': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'scp': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        u'django_mta.turnstiledownloadcomplete': {
            'Meta': {'object_name': 'TurnstileDownloadComplete'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['django_mta']