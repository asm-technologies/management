from django.core.management.base import NoArgsCommand
from employee.models import *
import random

class Command(NoArgsCommand):
    help = "prints hello world"

    def handle_noargs(self, **options):
    	des = ["B.E","B.Tech","MCA","MS","MSC","BSC","M.Tech","M.E","MBA"]
    	emp_ids = Employee.objects.filter().values('id')
    	for x in emp_ids:
    	 	emp_val = Employee.objects.get(id=x['id'])
    	 	emp_val.Qualification = random.choice(des)
    	 	# print emp_val.Visa_Status
    	 	emp_val.save()
        