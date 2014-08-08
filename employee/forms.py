from django import forms
from employee.models import *
def get_my_choices():
        choices_list =  Sub_Project.objects.all()
        MY_CHOICES = (('1', 'Option 1'),('2', 'Option 2'),('3', 'Option 3'),)
        print choices_list[0]
        return MY_CHOICES
        #return choices_list    

class AddBillingForm(forms.Form):
        emp_list = Employee.objects.filter()
        proj_list = Project.objects.filter()
        bill_type = ['Permanent','Temporary']
        Employee = forms.ModelChoiceField(queryset=Employee.objects.all())
        Project =  forms.ModelChoiceField(queryset=Project.objects.all())
        #Sub_Project = forms.ChoiceField(choices=get_my_choices())
        Sub_Project =  forms.ModelChoiceField(queryset=Sub_Project.objects.all())
        Billing_Type = forms.ChoiceField(choices=zip(bill_type,bill_type))
        Billing_Start_Date = forms.DateField(help_text="yyyy-dd-mm")
        Billing_End_Date = forms.DateField(help_text="yyyy-dd-mm")

