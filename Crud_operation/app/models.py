from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=100)
    Roll_no = models.IntegerField()
    City = models.CharField(max_length=100)
    