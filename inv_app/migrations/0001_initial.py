# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table('inv_app_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('role', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
        ))
        db.send_create_signal('inv_app', ['Person'])

        # Adding model 'Item'
        db.create_table('inv_app_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inv_app.Person'])),
            ('computer_type', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('os', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('other', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('inv_app', ['Item'])

        # Adding model 'Printer'
        db.create_table('inv_app_printer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('make', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('inv_app', ['Printer'])

        # Adding model 'Network'
        db.create_table('inv_app_network', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ip', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('inv_app', ['Network'])

        # Adding model 'Phone'
        db.create_table('inv_app_phone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inv_app.Person'])),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('inv_app', ['Phone'])

        # Adding model 'Monitor'
        db.create_table('inv_app_monitor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inv_app.Person'])),
            ('model', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('added_by', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('inv_app', ['Monitor'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table('inv_app_person')

        # Deleting model 'Item'
        db.delete_table('inv_app_item')

        # Deleting model 'Printer'
        db.delete_table('inv_app_printer')

        # Deleting model 'Network'
        db.delete_table('inv_app_network')

        # Deleting model 'Phone'
        db.delete_table('inv_app_phone')

        # Deleting model 'Monitor'
        db.delete_table('inv_app_monitor')


    models = {
        'inv_app.item': {
            'Meta': {'object_name': 'Item'},
            'computer_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'os': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'other': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inv_app.Person']"})
        },
        'inv_app.monitor': {
            'Meta': {'object_name': 'Monitor'},
            'added_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inv_app.Person']"})
        },
        'inv_app.network': {
            'Meta': {'object_name': 'Network'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'inv_app.person': {
            'Meta': {'object_name': 'Person'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        },
        'inv_app.phone': {
            'Meta': {'object_name': 'Phone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'model': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inv_app.Person']"})
        },
        'inv_app.printer': {
            'Meta': {'object_name': 'Printer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'make': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['inv_app']