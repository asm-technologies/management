# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Sub_Project.name'
        db.delete_column(u'employee_sub_project', 'name_id')

        # Adding field 'Sub_Project.Project'
        db.add_column(u'employee_sub_project', 'Project',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['employee.Project']),
                      keep_default=False)

        # Adding field 'Sub_Project.sub_proj'
        db.add_column(u'employee_sub_project', 'sub_proj',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=100),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Sub_Project.name'
        raise RuntimeError("Cannot reverse this migration. 'Sub_Project.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Sub_Project.name'
        db.add_column(u'employee_sub_project', 'name',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['employee.Project']),
                      keep_default=False)

        # Deleting field 'Sub_Project.Project'
        db.delete_column(u'employee_sub_project', 'Project_id')

        # Deleting field 'Sub_Project.sub_proj'
        db.delete_column(u'employee_sub_project', 'sub_proj')


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
            'Project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['employee.Project']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sub_proj': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['employee']