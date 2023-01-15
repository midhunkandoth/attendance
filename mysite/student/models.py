from django.db import models
from django.urls import reverse


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=100)
    number_of_years = models.IntegerField()
    hod = models.CharField(max_length=50)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    joining_date = models.DateField()
    create_date = models.DateField(auto_now_add=True)