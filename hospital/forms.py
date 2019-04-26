from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import apt,login
#from django.forms import ModelForm
class apt_form(forms.ModelForm): 
	class Meta :
		model = apt
		fields=('name','dob','age','phone','email','hospital','speciality')

class UserForm(forms.ModelForm):
	username=forms.CharField(max_length=30)
	password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = login
		fields=('username','password')

