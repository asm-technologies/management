from django.core.management.base import NoArgsCommand
from employee.models import *
import random
import datetime

class Command(NoArgsCommand):
    help = "prints hello world"

    def handle_noargs(self, **options):
    	proj_id = [2,3,5,6,7]
    	bill_ids = Billing_Detail.objects.filter().values('id')
        for x in bill_ids:
    	        bill_id = Billing_Detail.objects.get(id=x['id']) 	
                print x
                bill_id.emp_proj_id = (random.choice(proj_id))
                bill_id.save()
                # raw_input()

            # raw_input()

			#print emp_val.doj
    	 	# print emp_val.Visa_Status
    	 	#emp_val.save()
        
