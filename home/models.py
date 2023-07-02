from django.db import models

# Create your models here.

class Student(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    age= models.IntegerField()
    email= models.EmailField(max_length=255)
    phone= models.CharField(max_length=255)
    address= models.CharField(max_length=255)

    