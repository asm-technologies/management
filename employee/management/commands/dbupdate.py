from django.core.management.base import NoArgsCommand
from employee.models import *
import random
import datetime

class Command(NoArgsCommand):
    help = "prints hello world"

    def handle_noargs(self, **options):
    	des = ['Computer Science','Information Technology','Electronics','Management']
    	emp_ids = Employee.objects.filter().values('id')
    	for x in emp_ids:
    	 	emp_val = Employee.objects.get(id=x['id'])
		if emp_val.doj == None:
	    	 	emp_val.doj = datetime.date.today()
			#print emp_val.doj
    	 	# print emp_val.Visa_Status
    	 	emp_val.save()
        
