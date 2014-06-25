from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from employee.models import *
import datetime
import json

def project_json(request,proj_id):
	projs = Project.objects.filter().values()
	proj_values = []
	for x in projs:
		ID = x['id']
		name = x['name']
		description = x['description']
		proj_values.append({"ID":ID,"name":name,"description":description})
	if proj_id == 'null' :
		first_proj = projs[0]
		employees = Employee.objects.filter(proj=first_proj['id']).values()
	else:
		employees = Employee.objects.filter(proj=proj_id).values()
	
	response_list = []
	for x in employees:
				d1 =  datetime.date.today()
				d2 =  x['doj']
				yr_diff = (d1.year - d2.year)*12 + d1.month - d2.month
				x['asm_exp'] = "%s.%s" % (yr_diff/12,yr_diff%12)
				name = '<a href="javascript:poptastic(\'/employee/%d/\');">%s</a>' % (x['id'],x['name'])
				response_list.append([x['id'],name,str(x['exp']),str(x['doj']),str(x['asm_exp']),str(x['start_date']),str(x['bill'])])
	#response_data = {"aaData":[[1,'naggappan',1.5,'April 30, 2013',2.5,'April 2, 2014',True],[2,'naggappan',1.5,'April 30, 2013',2.5,'April 2, 2014',True]]}
	response_data = {"aaData":response_list}
	return HttpResponse(json.dumps(response_data), content_type="application/json")

def employees_main(request):
	all_employee = Employee.objects.filter().values()
	for x in all_employee:
		projs = Project.objects.filter(id=x['proj_id']).values()
		x['proj'] = projs[0]['name']
	return render_to_response("employee_main.html",{"employee":"active",'all_employee':all_employee},context_instance=RequestContext(request))

def employees(request,emp_id):
	employees = Employee.objects.filter(id=emp_id).values()
	return render_to_response("employee.html",{"employee":"active",'employees':employees[0]},context_instance=RequestContext(request))

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
	
	
