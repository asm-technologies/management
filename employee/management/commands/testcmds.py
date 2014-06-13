from django.core.management.base import NoArgsCommand
from employee.models import *
import random
import datetime
from decimal import *
class Command(NoArgsCommand):
    help = "prints hello world"

    def handle_noargs(self, **options):
			projs = Project.objects.filter().values()
			proj_values = []
			for x in projs:
				ID = x['id']
				name = x['name']
				description = x['description']
				proj_values.append({"ID":ID,"name":name,"description":description})
			first_proj = projs[0]
			employees = Employee.objects.filter(proj=first_proj['id']).values()
			for x in employees:
				d1 =  datetime.date.today()
				d2 =  x['doj']
				yr_diff = (d1.year - d2.year)*12 + d1.month - d2.month
				print "%s.%s" % (yr_diff/12,yr_diff%12)
				x['asm_exp'] = "%s.%s" % (yr_diff/12,yr_diff%12)
				print x
				
				raw_input()