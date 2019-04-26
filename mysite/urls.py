"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital.views import apt_create_view,doc_list_derm,doc_list_cardio,doc_list_gynic,doc_list_ENT,doc_list_pedo,doc_list_onco,doc_list_neuro,login_view,signup
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from django.conf.urls import url,include


urlpatterns = [
    path('admin/',admin.site.urls),
    url(r'create/$',apt_create_view),
    url(r'OmegaHospitals/$',TemplateView.as_view(template_name='home.html'),name='home'),
    url(r'signup/$',signup),
   # url(r'signup/$',Signup,name='signup'),
    url(r'derm/$',doc_list_derm),
    url(r'cardio/$',doc_list_cardio),
    url(r'gynic/$',doc_list_gynic),
    url(r'ENT/$',doc_list_ENT),
    url(r'pedo/$',doc_list_pedo),
    url(r'onco/$',doc_list_onco),
    url(r'neuro/$',doc_list_neuro),
    url(r'login/$',login_view),
    url(r'logdin/$',TemplateView.as_view(template_name='logged_in.html'),name='logd'),
]

urlpatterns+=staticfiles_urlpatterns()