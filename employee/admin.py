from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from employee.models import *
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
	search_fields = ['name']
	list_display = ('name','bill')
	list_filter = ('bill','proj')
	#inlines = [ UserProfileInline, ]

# admin.site.unregister(Account)
# admin.site.unregister(Eventlog)
# admin.site.unregister(Sites)
admin.site.register( Employee, EmployeeAdmin )
admin.site.register( Project )
