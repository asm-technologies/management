# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'employee_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=254)),
        ))
        db.send_create_signal(u'employee', ['Project'])

        # Adding model 'Employee'
        db.create_table(u'employee_employee', (
            ('id', self.gf('django.db.models.fields.IntegerField')(max_length=6, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('doj', self.gf('django.db.models.fields.DateField')()),
            ('exp', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('Designation', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Qualification', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('Major_Subject', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('Visa_Status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Skill_sets', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('Add1', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('Add2', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('City', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('Zip_code', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('mobile', self.gf('django.db.models.fields.IntegerField')(max_length=12)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
            ('personal_email', self.gf('django.db.models.fields.EmailField')(max_length=50, blank=True)),
            ('bill', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('proj', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employee.Project'])),
            ('start_date', self.gf('django.db.models.fields.DateField')(blank=True)),
        ))
        db.send_create_signal(u'employee', ['Employee'])

        # Adding model 'MonthlyWeatherByCity'
        db.create_table(u'employee_monthlyweatherbycity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('month', self.gf('django.db.models.fields.IntegerField')()),
            ('boston_temp', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('houston_temp', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
        ))
        db.send_create_signal(u'employee', ['MonthlyWeatherByCity'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'employee_project')

        # Deleting model 'Employee'
        db.delete_table(u'employee_employee')

        # Deleting model 'MonthlyWeatherByCity'
        db.delete_table(u'employee_monthlyweatherbycity')


    models = {
        u'employee.employee': {
            'Add1': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'Add2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'City': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'Designation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Major_Subject': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'Meta': {'object_name': 'Employee'},
            'Qualification': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'Skill_sets': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Visa_Status': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'Zip_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'bill': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'doj': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'exp': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'max_length': '6', 'primary_key': 'True'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'personal_email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'proj': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Project']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True'})
        },
        u'employee.monthlyweatherbycity': {
            'Meta': {'object_name': 'MonthlyWeatherByCity'},
            'boston_temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'houston_temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {})
        },
        u'employee.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['employee']