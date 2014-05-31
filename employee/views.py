from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#from chartit import DataPool, Chart

from employee.models import *

# Create your views here.

# def home(request):
#  	return render_to_response("homepage.html",context_instance=RequestContext(request))

def employee(request):
	return render_to_response("employee.html",{"employee":"active"},context_instance=RequestContext(request))

def projects(request):
	projs = Project.objects.filter().values()
	proj_values = []
	for x in projs:
		ID = x['id']
		name = x['name']
		description = x['description']
		proj_values.append({"ID":ID,"name":name,"description":description})
	return render_to_response("projects.html",{"projects":"active","proj_values":proj_values},context_instance=RequestContext(request))

def home(request):
	available_pjs = Project.objects.filter().values('id')
	dict1 = []
	for x in available_pjs:
		ID = x['id']
		proj_name = Project.objects.filter(id=ID).values('name')[0]['name']
		project = Employee.objects.filter(proj=ID).count()
		not_bill = Employee.objects.filter(proj=ID,bill=0).count()
		dict1.append({"ID":ID,"proj_name":proj_name,"project":project,"not_bill":not_bill})
		
		dict2 = dict1[:]
	

	return render_to_response("homepage.html",{"home":"active",'mylist':dict1,"mylist2":dict2},context_instance=RequestContext(request))