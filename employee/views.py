from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from decimal import *
from employee.models import *
import datetime
import json

from employee.forms import AddBillingForm
from django.http import HttpResponseRedirect

def project_json(request,proj_id):
	response_list = []
	tmp = {}
	all_employee = Employee.objects.filter().values()
	dist_emp_billing = Billing_Detail.objects.filter().values('emp_name_id').distinct()
	for emp in all_employee:
		tmp['emp_id'] = emp['id']
		tmp['name'] = '<a href="javascript:poptastic(\'/employee/%d/\');">%s</a>' % (emp['id'],emp['name'])
		tmp['bill'] = 'NO'
		tmp['project'] = 'Not Assigned'
		tmp['bill_type'] = 'Not Assigned'
		tmp['start_bill'] = 'None'
		tmp['end_bill'] = 'None'
		for x in dist_emp_billing:
			if emp['id'] == x['emp_name_id']:
				emp_billing = Billing_Detail.objects.filter(emp_name_id=emp['id']).values().order_by('end_date')
				if emp_billing[0]['bill_type'] == 'Permanent' :
					emp_value = Billing_Detail.objects.get(id=emp_billing[0]['id'])
					tmp['project'] = emp_value.emp_proj.name
					tmp['bill'] = 'YES'
					tmp['bill_type'] = 'Permanent'
				if emp_billing[0]['bill_type'] == 'Temporary' :
					
					tmp['project'] = emp_value.emp_proj.name
					tmp['bill_type'] = 'Temporary'
					tmp['start_bill'] = str(emp_billing[0]['start_date'])
					tmp['end_bill'] = str(emp_billing[0]['end_date'])
					if tmp['end_bill'] == 'None' and tmp['start_bill'] != 'None':
					 	tmp['bill'] = 'YES'

				# for bill in emp_billing:
		bill_query = [tmp['emp_id'],tmp['name'],tmp['project'],tmp['bill'],tmp['bill_type'],tmp['start_bill'],tmp['end_bill']]
		response_list.append(bill_query)
	
	response_data = {"aaData":response_list}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def employees_main(request):
	all_employee = Employee.objects.filter().values()
	for x in all_employee:
		projs = Project.objects.filter(id=x['proj_id']).values()
		x['proj'] = projs[0]['name']
		d1 =  datetime.date.today()
		d2 =  x['doj']
		yr_diff = (d1.year - d2.year)*12 + d1.month - d2.month
		x['asm_exp'] = "%s.%s" % (yr_diff/12,yr_diff%12)
		x['Total_exp'] = Decimal(x['asm_exp']) + Decimal(x['exp'])
	return render_to_response("employee_main.html",{"employee":"active",'all_employee':all_employee},context_instance=RequestContext(request))

def employees(request,emp_id):
	employees = Employee.objects.filter(id=emp_id).values()
	bill_value = Billing_Detail.objects.filter(emp_name_id=emp_id).values().order_by('end_date')
	bill_hist_list = []
	for each_entry in bill_value:
		tmp = {}
		bill_hist = Billing_Detail.objects.get(id=each_entry['id'])
		tmp['start_date'] = bill_hist.start_date
		tmp['end_date'] = bill_hist.end_date
		tmp['proj_name'] = bill_hist.emp_proj.name
		bill_hist_list.append(tmp)
	print bill_hist_list

	return render_to_response("employee.html",{"employee":"active",'employees':employees[0],'billing_history':bill_hist_list},context_instance=RequestContext(request))

def projects_main(request):
	projs = Project.objects.filter().values()
	proj_values = []
	for x in projs:
		ID = x['id']
		name = x['name']
		description = x['description']
		proj_values.append({"ID":ID,"name":name,"description":description})
	return render_to_response("projects_main.html",{"projects":"active","proj_values":proj_values},context_instance=RequestContext(request))

def home(request):
	available_pjs = Project.objects.filter().values('id')
	dict1 = []
	for x in available_pjs:
		ID = x['id']
		proj_name = Project.objects.filter(id=ID).values('name')[0]['name']
		bill = Employee.objects.filter(proj=ID,bill=1).count()
		not_bill = Employee.objects.filter(proj=ID,bill=0).count()
		dict1.append({"proj_name":proj_name,"bill":bill,"not_bill":not_bill,"ID":ID})
		
		dict2 = dict1[:]
	return render_to_response("homepage.html",{"home":"active",'mylist':dict1,"mylist2":dict2},context_instance=RequestContext(request))

def addbilling(request):
	if request.method == 'GET':
		#form = AddBillingForm()
		form=AddBillingForm()
	else:
 	    #A POST request
	    form = AddBillingForm(request.POST)
	    print "form status----------------"
	    print form.is_valid()
	    
	    if form.is_valid():
			print "success validation"
			form.save()
            return HttpResponseRedirect('/thanks')

	return render(request, 'addbilling.html', {'form': form,})

	
	
#### Test for sample 	
