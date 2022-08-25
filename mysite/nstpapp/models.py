from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.timezone import now
from datetime import timedelta





class extenduser(models.Model):
    #first part of registration
    firstname = models.CharField(max_length=30, default='', null=True)
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
    field = models.CharField(max_length=20, default='Select Course')
    picture = models.ImageField(upload_to='images/', null=False)
    status = models.CharField(max_length=10, default='PENDING')
    platoons = models.CharField(max_length=20, default='')
    
    # additionals

    civil = models.CharField(max_length=20, default='')
    nfather = models.CharField(max_length=20, default='')
    foccupation = models.CharField(max_length=20, default='')
    nmother = models.CharField(max_length=20, default='')
    moccupation = models.CharField(max_length=20, default='')
    pcontact = models.CharField(max_length=20, default='')
    
    nguardian = models.CharField(max_length=20, default='')
    goccupation = models.CharField(max_length=20, default='')
    gcontact = models.CharField(max_length=20, default='')
    
    idpic = models.ImageField(upload_to="images/", default='' )
    disease  = models.CharField(max_length=100, default='')
    specific = models.CharField(max_length=100, default='')
    proof = models.FileField(upload_to='proofs/', default='')
    s_year = models.CharField(max_length=100, default='0000')


    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return self.idnumber
    
class school_year(models.Model):
    years = models.CharField(max_length=20, default='')
    
class sections(models.Model):
    section_created = models.CharField(max_length=20, default='')

    
