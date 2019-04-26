from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.contrib.auth.forms import UserCreationForm
from .models import apt,doctor
from .forms import apt_form,UserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic

def apt_create_view(request):
	if request.method=="POST":
		form = apt_form(request.POST or None)
		if form.is_valid():
			apt=form.save(commit=True)
			
	else:
		form=apt_form()

	return render(request,"hospital/apt_create_view.html",{'form':form})

def doc_list_derm(request):
	doctors= doctor.objects.filter(speciality='Dermatology')
	return render (request,'hospital/doc_list_derm.html',{'doctors':doctors})

def doc_list_cardio(request):
	doctors= doctor.objects.filter(speciality='Cardiology')
	return render (request,'hospital/doc_list_derm.html',{'doctors':doctors})

def doc_list_ENT(request):
	doctors= doctor.objects.filter(speciality='ENT')
	return render (request,'hospital/doc_list_derm.html',{'doctors':doctors})

def doc_list_gynic(request):
	doctors= doctor.objects.filter(speciality='Gynecology')
	return render (request,'hospital/doc_list_derm.html',{'doctors':doctors})
def doc_list_neuro(request):
	doctors= doctor.objects.filter(speciality='Neurology')
	return render (request,'hospital/doc_list_derm.html',{'doctors':doctors})
def doc_list_onco(request):
	doctors= doctor.objects.filter(speciality='Oncology')
	return render (request,'hospital/doc_list_derm.html',{'doctors':doctors})
def doc_list_pedo(request):
	doctors= doctor.objects.filter(speciality='Pediatrics')
	return render (request,'hospital/doc_list_derm.html',{'doctors':doctors})
def login_view(request):
	form=UserForm(request.POST)
	return render(request,'registration/login.html',{'form':form})
'''def login_val(request):'''

'''class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'''

	
def signup(request):
	form=UserCreationForm(request.POST)
	if request.method=='POST':
		if form.is_valid():
			form.save()
			return redirect('OmegaHospitals/')
		else:
			form=UserCreationForm()
	return render(request,'registration/signup.html',{'form':form})
	