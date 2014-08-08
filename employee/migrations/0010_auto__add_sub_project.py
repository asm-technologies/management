# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sub_Project'
        db.create_table(u'employee_sub_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employee.Project'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
        ))
        db.send_create_signal(u'employee', ['Sub_Project'])


    def backwards(self, orm):
        # Deleting model 'Sub_Project'
        db.delete_table(u'employee_sub_project')


    models = {
        u'employee.billing_detail': {
            'Meta': {'object_name': 'Billing_Detail'},
            'bill_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'emp_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Employee']"}),
            'emp_proj': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Project']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.IntegerField', [], {'max_length': '12'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'personal_email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'proj': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Project']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True'})
        },
        u'employee.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'employee.sub_project': {
            'Meta': {'object_name': 'Sub_Project'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Project']"})
        }
    }

    complete_apps = ['employee']