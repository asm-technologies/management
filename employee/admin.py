from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from employee.models import *
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
	search_fields = ['name','id']
	list_display = ('id','name','dob','bill','mobile','email')
	list_filter = ('bill','proj')
	#readonly_fields=('id',)

	def get_readonly_fields(self,request,obj=None):
		if obj:   # editing an existing object
			return self.readonly_fields + ('id',)
		return self.readonly_fields


# admin.site.unregister(Account)
# admin.site.unregister(Eventlog)
# admin.site.unregister(Sites)
admin.site.register( Employee, EmployeeAdmin )
admin.site.register( Project )
