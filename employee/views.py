from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from employee.models import *


def employee(request):
	available_pjs = Employee.objects.filter().values('id')
	dict1 = []
	for x in available_pjs:
		ID = x['id']
		emp_name = Employee.objects.filter(id=ID).values('name')[0]['name']
		mobile = Employee.objects.filter(id=ID).values('mobile')[0]['mobile']
		email = Employee.objects.filter(id=ID).values('email')[0]['email']
		dict1.append({"emp_name":emp_name,"mobile":mobile,"email":email,"ID":ID})
	return render_to_response("employee.html",{"employee":"active",'mylist':dict1},context_instance=RequestContext(request))
	

def projects_main(request):
	projs = Project.objects.filter().values()
	proj_values = []
	for x in projs:
		ID = x['id']
		name = x['name']
		description = x['description']
		proj_values.append({"ID":ID,"name":name,"description":description})
	first_proj = projs[0]
	employees = Employee.objects.filter(proj=first_proj['id']).values()
	return render_to_response("projects_main.html",{"projects":"active","proj_values":proj_values,"first_proj":first_proj,"employees":employees},context_instance=RequestContext(request))

def projects(request,proj_id):
	proj = Project.objects.filter(id=proj_id).values()
	proj_values = Project.objects.filter().values()
	employees = Employee.objects.filter(proj=proj_id).values()
	return render_to_response("projects.html",{"projects":"active","proj":proj[0],"employees":employees,"proj_values":proj_values},context_instance=RequestContext(request))

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
	
	
