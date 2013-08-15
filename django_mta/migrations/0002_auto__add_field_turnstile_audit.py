# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Turnstile.audit'
        db.add_column(u'django_mta_turnstile', 'audit',
                      self.gf('django.db.models.fields.CharField')(default='REGULAR', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Turnstile.audit'
        db.delete_column(u'django_mta_turnstile', 'audit')


    models = {
        u'django_mta.turnstile': {
            'Meta': {'object_name': 'Turnstile'},
            'audit': ('django.db.models.fields.CharField', [], {'default': "'REGULAR'", 'max_length': '20'}),
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