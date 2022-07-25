from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class extenduser(models.Model):
    #first part of registration
    firstname = models.CharField(max_length=30, default='')
    lastname = models.CharField(max_length=30, default='')
    middlename = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=254, null=True, unique=True)
    idnumber = models.CharField(max_length=30, default='')
    password = models.CharField(max_length=20)
    
    address = models.CharField(max_length=100, default='')
    cpnumber = models.CharField(max_length=100, default='')
    gender = models.CharField(max_length=6, default='')
    age = models.CharField(max_length=3, default='', null=True)
    birthday = models.CharField(max_length=15, default='')
    section = models.CharField(max_length=20, default='')
    field = models.CharField(max_length=20, default='')
    picture = models.ImageField(upload_to='images/', null=False)
    status = models.CharField(max_length=10, default='PENDING')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.email
    