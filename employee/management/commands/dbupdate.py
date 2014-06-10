from django.core.management.base import NoArgsCommand
from employee.models import *
import random

class Command(NoArgsCommand):
    help = "prints hello world"

    def handle_noargs(self, **options):
    	des = ['Computer Science','Information Technology','Electronics','Management']
    	emp_ids = Employee.objects.filter().values('id')
    	for x in emp_ids:
    	 	emp_val = Employee.objects.get(id=x['id'])
    	 	emp_val.Major_Subject = random.choice(des)
    	 	# print emp_val.Visa_Status
    	 	emp_val.save()
        
