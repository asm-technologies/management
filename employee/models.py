from django.db import models

# Create your models here.


class Project(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 254)

	def __unicode__(self):
		return u"%s" % (self.name)

class Employee(models.Model):
	id = models.IntegerField(max_length = 6,primary_key=True,verbose_name="Employee ID")
	name = models.CharField(max_length = 100,verbose_name="Name")
	dob = models.DateField(verbose_name='Date Of Birth')
	doj = models.DateField(verbose_name='Date Of Joining')
	exp = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="Year of Experience")
	Designation = models.CharField(max_length = 100)
	Qualification = models.CharField(max_length = 100)
	Visa_Status = models.CharField(max_length = 100)
	Skill_sets = models.CharField(max_length = 100)
	# qualif_choices = ['BE','B.Tech','MBA','MS','MCA']
	# qualif = models.CharField(max_length=10,choices=qualif,default=BE)
	mobile=models.IntegerField(max_length = 12)
	email = models.EmailField(max_length=50)
	personal_email = models.EmailField(max_length=50,blank=True)
	bill = models.BooleanField(db_index=True,default=False)
	proj = models.ForeignKey(Project)
	start_date = models.DateField(blank=True)

	def __unicode__(self):
		return u"%s" % (self.name)




class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)
