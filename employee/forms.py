from django import forms
from django.forms import ModelForm
from employee.models import *

def get_my_choices():
        choices_list =  Sub_Project.objects.all()
        MY_CHOICES = (('1', 'Option 1'),('2', 'Option 2'),('3', 'Option 3'),)
        print choices_list[0]
        return MY_CHOICES
        #return choices_list    

class AddBillingForm(ModelForm):
        class Meta:
                model = Billing_Detail
                widgets = {'start_date': forms.DateInput(attrs={'class':'datepicker'}),}



