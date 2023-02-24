from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from app.models import *
# Create your views here.
class school_list(ListView):
    model=School
    context_object_name='schools'
    #template_name='app/School_list.html'
    #queryset=School.objects.all()
    ordering=['name']
class School_details(DetailView):
    model=School
    context_object_name='sc'
    

class Homepage(TemplateView):
    template_name='app/Homepage.html'