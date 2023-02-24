from django.db import models
from django.http import HttpResponse
from django.urls import reverse
# Create your models here.
class School(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    principal=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('')



class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    school=models.ForeignKey(School,on_delete=models.CASCADE)
    def __str__(self):
        return  self.name

