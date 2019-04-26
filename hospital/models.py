from django.db import models
from django.conf import settings
from django.utils import timezone



# Create your models here.

class apt(models.Model):
	#class Meta:
	#	model = Appointment
	#	fields=('name','gender','dob','age','phone','email','hospital','speciality','appointment_category',)

	gender_choices={
	('M','Male'),
	('F','Female')
	}

	hospital_choices={
	('jayanagar','omega hospitals,jayanagr'),
	('vijayanagar','omega hospitals,vijayanagar'),
	('girinagar','omega hospitals,girinagar')
	}

	speciality_choices={
	('dermetalogy','dermetalogy'),
	('cardiology','cardiology'),
	('ENT','ENT'),
	('oncology','oncology'),
	('pediatrics','pediatrics'),
	('gynecology','gynecology')
	}

	apt_choices={
	('first visit','first'),
	('follow up visit','follow up')
	}
	name=models.CharField(max_length=20)
	#gender=models.CharField(choices=gender_choices,widget=models.RadioSelect())
	dob=models.DateTimeField()
	age=models.PositiveSmallIntegerField()
	phone=models.DecimalField(decimal_places=0,max_digits=10)
	email=models.EmailField(max_length=70)
	hospital=models.CharField(max_length=30,choices=hospital_choices,default='girinagar')
	speciality=models.CharField(max_length=30,choices=speciality_choices,default='pediatrcis')
	#appointment_category=models.CharField(widget=models.RadioSelect(choices=apt_choices))


class doctor(models.Model):
		name=models.CharField(max_length=50)
		qualifications=models.CharField(max_length=70)
		designation=models.CharField(max_length=50)
		speciality=models.CharField(max_length=50)
		location=models.CharField(max_length=30)
class login(models.Model):
		username=models.CharField(max_length=30)
		password=models.CharField(max_length=10)