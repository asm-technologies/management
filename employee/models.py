from django.db import models

# Create your models here.


class Project(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 254)

	def __unicode__(self):
		return u"%s" % (self.name)

class Employee(models.Model):
	name = models.CharField(max_length = 100)
	bill = models.BooleanField(db_index=True,default=False)
	proj = models.ForeignKey(Project)
	start_date = models.DateField()

	def __unicode__(self):
		return u"%s" % (self.name)

class MonthlyWeatherByCity(models.Model):
    month = models.IntegerField()
    boston_temp = models.DecimalField(max_digits=5, decimal_places=1)
    houston_temp = models.DecimalField(max_digits=5, decimal_places=1)