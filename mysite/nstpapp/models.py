from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.utils.timezone import now
from datetime import timedelta

# from mysite.nstpapp.views import school_years




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
    
    # attendance
    TD1= models.CharField(max_length=100, default='')
    TD2= models.CharField(max_length=100, default='')
    TD3= models.CharField(max_length=100, default='')
    TD4= models.CharField(max_length=100, default='')
    TD5= models.CharField(max_length=100, default='')
    TD6= models.CharField(max_length=100, default='')
    TD7= models.CharField(max_length=100, default='')
    TD8= models.CharField(max_length=100, default='')
    TD9= models.CharField(max_length=100, default='')
    TD10= models.CharField(max_length=100, default='')
    TD11= models.CharField(max_length=100, default='')
    TD12= models.CharField(max_length=100, default='')
    TD13= models.CharField(max_length=100, default='')
    TD14= models.CharField(max_length=100, default='')
    TD15= models.CharField(max_length=100, default='')
    
    
    
    def __str__(self):
        return self.idnumber
    
class school_year(models.Model):
    years = models.CharField(max_length=20, default='')
    status = models.CharField(max_length=20, default='OPEN')
    acts = models.CharField(max_length=20, default='PENDING')
    date_generated = models.DateField(max_length=40, default='PENDING')
    
    # for certificates
    
    commandant = models.CharField(max_length=20, default='')
    registrar = models.CharField(max_length=20, default='')
    month = models.CharField(max_length=20, default='')
    date = models.CharField(max_length=20, default='')
    year = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.years

class sections(models.Model):
    fiel = models.CharField(max_length=20, default='')
    section_created = models.CharField(max_length=20, default='', primary_key=True)
    
class training_day(models.Model):
    title =  models.CharField(max_length=20, default='')


    

    def __str__(self):
        return self.title
    
class Announcement(models.Model):
    assign = models.CharField(max_length=20, default='')
    subject = models.CharField(max_length=20, default='')
    content = models.CharField(max_length=500, default='')
    date_posted = models.DateTimeField(default='')
    
    def __str__(self):
        return self.subject
    
class certification(models.Model):
    
    # for rotc
    school_year2 = models.CharField(max_length=20, default='')
    commandant = models.CharField(max_length=40, default='')
    registrar = models.CharField(max_length=40, default='')
    month = models.CharField(max_length=20, default='')
    date = models.CharField(max_length=20, default='')
    year = models.CharField(max_length=20, default='')
    
        
    def __str__(self):
        return self.year
    
    

    
