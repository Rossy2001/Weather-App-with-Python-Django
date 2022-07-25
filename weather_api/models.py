from turtle import distance
from django.db import models

# Create your models here.

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile = models.CharField(max_length=15,default='')
    message=models.TextField(max_length=150)
    def __str__(self):
        return self.name

class Search(models.Model):
    address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address

