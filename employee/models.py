from django.db import models

# Create your models here.


class Project(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 254)

	def __unicode__(self):
		return u"%s" % (self.name)

class Employee(models.Model):
	name = models.CharField(max_length = 100)
	dob = models.DateField(verbose_name='Date Of Birth')
	doj = models.DateField(verbose_name='Date Of Joining')
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
