from django.db import models

# Create your models here.


class Project(models.Model):
	name = models.CharField(max_length = 100)
	description = models.CharField(max_length = 254)

	def __unicode__(self):
		return u"%s" % (self.name)

def upload_image_name(instance, filename):
    extension = filename.split('.')[-1]
    return "%s.%s" %(instance.id, extension)

class Employee(models.Model):
	qualif_choices = [('B.E','B.E'),('B.Tech','B.Tech'),('M.Tech','M.Tech'),('BSC','BSC'),('MCA','MCA'),('MS','MS'),('M.E','M.E'),('MS','MS'),('MSC','MSC'),('MBA','MBA')]
	sub_choices = [('Computer Science','Computer Science'),('Information Technology','Information Technology'),('Electornics','Electronics'),('Management','Management')]
	id = models.IntegerField(max_length = 6,primary_key=True,verbose_name="Employee ID")
	name = models.CharField(max_length = 100,verbose_name="Name")
	image = models.ImageField(upload_to = upload_image_name,blank=True,null=True)
	dob = models.DateField(verbose_name='Date Of Birth')
	doj = models.DateField(verbose_name='Date Of Joining')
	exp = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="Eperience Previous to ASM")
	Designation = models.CharField(max_length = 100)
	Qualification = models.CharField(max_length = 10,choices=qualif_choices)
	Major_Subject = models.CharField(max_length = 100,blank=True,choices=sub_choices)
	Visa_Status = models.CharField(max_length = 100)
	Skill_sets = models.CharField(max_length = 100)
	Add1 = models.CharField(max_length = 250,blank=True,verbose_name='Line1')
	Add2 = models.CharField(max_length = 250,blank=True,verbose_name='Line2')
	City = models.CharField(max_length = 30,blank=True)
	Zip_code = models.CharField(max_length = 15,blank=True)
	mobile=models.IntegerField(max_length = 12)
	email = models.EmailField(max_length=50)
	personal_email = models.EmailField(max_length=50,blank=True)
	bill = models.BooleanField(db_index=True,default=False)
	proj = models.ForeignKey(Project)
	start_date = models.DateField(blank=True,verbose_name='Billing Start Date')

	def __unicode__(self):
		return u"%s" % (self.name)

