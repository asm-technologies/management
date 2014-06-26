from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from eventlog.models import Log
from account.models import Account, SignupCode, AccountDeletion, EmailAddress

# Register your models here.

admin.site.unregister(Log)

admin.site.unregister(Account)
admin.site.unregister(SignupCode)
admin.site.unregister(AccountDeletion)
admin.site.unregister(EmailAddress)
admin.site.unregister(Group)
# admin.site.unregister( Sites )


