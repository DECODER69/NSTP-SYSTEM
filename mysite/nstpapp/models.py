from email.policy import default
from wsgiref.handlers import format_date_time
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
    platoons = models.CharField(max_length=20, default='PROCESSING')
    
    
    
    # additionals parents

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
    att_credits = models.CharField(max_length=100, default='')
    
    
        # merits
    TD1_dem= models.CharField(max_length=100, default='')
    TD2_dem= models.CharField(max_length=100, default='')
    TD3_dem= models.CharField(max_length=100, default='')
    TD4_dem= models.CharField(max_length=100, default='')
    TD5_dem= models.CharField(max_length=100, default='')
    TD6_dem= models.CharField(max_length=100, default='')
    TD7_dem= models.CharField(max_length=100, default='')
    TD8_dem= models.CharField(max_length=100, default='')
    TD9_dem= models.CharField(max_length=100, default='')
    TD10_dem= models.CharField(max_length=100, default='')
    TD11_dem= models.CharField(max_length=100, default='')
    TD12_dem= models.CharField(max_length=100, default='')
    TD13_dem= models.CharField(max_length=100, default='')
    TD14_dem= models.CharField(max_length=100, default='')
    TD15_dem= models.CharField(max_length=100, default='')
    first_merits = models.CharField(max_length=20, default='100')
    equivalent_merits = models.CharField(max_length=20, default='')
    
        # attendance 2nd semester
    TD1_2= models.CharField(max_length=100, default='')
    TD2_2= models.CharField(max_length=100, default='')
    TD3_2= models.CharField(max_length=100, default='')
    TD4_2= models.CharField(max_length=100, default='')
    TD5_2= models.CharField(max_length=100, default='')
    TD6_2= models.CharField(max_length=100, default='')
    TD7_2= models.CharField(max_length=100, default='')
    TD8_2= models.CharField(max_length=100, default='')
    TD9_2= models.CharField(max_length=100, default='')
    TD10_2= models.CharField(max_length=100, default='')
    TD11_2= models.CharField(max_length=100, default='')
    TD12_2= models.CharField(max_length=100, default='')
    TD13_2= models.CharField(max_length=100, default='')
    TD14_2= models.CharField(max_length=100, default='')
    TD15_2= models.CharField(max_length=100, default='')
    att_credits_2 = models.CharField(max_length=100, default='')
    
    
    
    #demerits sencond sem
    TD1_2_dem= models.CharField(max_length=100, default='')
    TD2_2_dem= models.CharField(max_length=100, default='')
    TD3_2_dem= models.CharField(max_length=100, default='')
    TD4_2_dem= models.CharField(max_length=100, default='')
    TD5_2_dem= models.CharField(max_length=100, default='')
    TD1_2_dem= models.CharField(max_length=100, default='')
    TD1_2_dem= models.CharField(max_length=100, default='')
    TD1_2_dem= models.CharField(max_length=100, default='')
    TD1_2_dem= models.CharField(max_length=100, default='')
    TD1_2_dem= models.CharField(max_length=100, default='')
    TD1_2_dem= models.CharField(max_length=100, default='')
    TD1_2_dem= models.CharField(max_length=100, default='')
    TD1_2_dem= models.CharField(max_length=100, default='')
    TD1_2_dem= models.CharField(max_length=100, default='')
    TD1_2_dem= models.CharField(max_length=100, default='')
    second_merits = models.CharField(max_length=20, default='100')
    equivalent_merits2 = models.CharField(max_length=20, default='')
        
        
    
    # activities
    act1 = models.CharField(max_length=20, default='')
    act2 = models.CharField(max_length=20, default='')
    act3 = models.CharField(max_length=20, default='')
    act4 = models.CharField(max_length=20, default='')
    act5 = models.CharField(max_length=20, default='')
    act6 = models.CharField(max_length=20, default='')
    all_act_score = models.CharField(max_length=20, default='')
    act_credits = models.CharField(max_length=20, default='')
    
        # activities 2nd semester
    act1_2 = models.CharField(max_length=20, default='')
    act2_2 = models.CharField(max_length=20, default='')
    act3_2 = models.CharField(max_length=20, default='')
    act4_2 = models.CharField(max_length=20, default='')
    act5_2 = models.CharField(max_length=20, default='')
    act6_2 = models.CharField(max_length=20, default='')
    all_act_score2 = models.CharField(max_length=20, default='')
    act_credits_2 = models.CharField(max_length=20, default='')
    
    
    # exercises
    
    # 1st sem
    exe1 = models.CharField(max_length=20, default='')
    exe2 = models.CharField(max_length=20, default='')
    exe3 = models.CharField(max_length=20, default='')
    exe4 = models.CharField(max_length=20, default='')
    exe5 = models.CharField(max_length=20, default='')
    exe6 = models.CharField(max_length=20, default='')
    exe7 = models.CharField(max_length=20, default='')
    exe8 = models.CharField(max_length=20, default='')
    exe9 = models.CharField(max_length=20, default='')
    exe10 = models.CharField(max_length=20, default='')
    exe_credits = models.CharField(max_length=20, default='')
    
    
    # 2nd sem
    
    exe1_2 = models.CharField(max_length=20, default='')
    exe2_2 = models.CharField(max_length=20, default='')
    exe3_2 = models.CharField(max_length=20, default='')
    exe4_2 = models.CharField(max_length=20, default='')
    exe5_2 = models.CharField(max_length=20, default='')
    exe6_2 = models.CharField(max_length=20, default='')
    exe7_2 = models.CharField(max_length=20, default='')
    exe8_2 = models.CharField(max_length=20, default='')
    exe9_2 = models.CharField(max_length=20, default='')
    exe10_2 = models.CharField(max_length=20, default='')
    exe_credits2 = models.CharField(max_length=20, default='')
    

    
    
    midterm1 = models.CharField(max_length=20, default='')
    midterm1_credits = models.CharField(max_length=20, default='')
    
    
    midterm2 = models.CharField(max_length=20, default='')
    midterm2_credits = models.CharField(max_length=20, default='')
    
    finals1 = models.CharField(max_length=20, default='')
    finals_credits1 = models.CharField(max_length=20, default='')
    
    finals2 = models.CharField(max_length=20, default='')
    finals_credits2 = models.CharField(max_length=20, default='')
    
    first_sem = models.CharField(max_length=20, default='')
    second_sem = models.CharField(max_length=20, default='')
    
    
    
    
    final_grade = models.CharField(max_length=20, default='')
    final_grade_2 = models.CharField(max_length=20, default='')
    
    first_equivalents = models.CharField(max_length=20, default='')
    second_equivalents = models.CharField(max_length=20, default='')
    
    # date_enrolled = models.DateTimeField(max_length=40, default='WAITING')
    
    
    def __str__(self):
        return self.idnumber
    
class school_year(models.Model):
    years = models.CharField(blank=True, null=True, max_length=20)
    sem = models.CharField(max_length=20, default='1st Sem')
    acts = models.CharField(max_length=20, default='PENDING')
    date_generated = models.DateTimeField(null=True)
    
    # for certificates
    
    commandant = models.CharField(max_length=20, default='')
    registrar = models.CharField(max_length=20, default='')
    month = models.CharField(max_length=20, default='')
    date = models.CharField(max_length=20, default='')
    year = models.CharField(max_length=20, default='')
    status = models.CharField(max_length=20, default='')
    def __str__(self):
        return self.years

class sections(models.Model):
    fiel = models.CharField(max_length=20, default='')
    section_created = models.CharField(max_length=20, default='', primary_key=True)
    
class training_day(models.Model):
    td = models.DateField(blank= True,null=True)
    td_count = models.CharField(max_length=254, default='')
    def __str__(self):
        return self.td
    
class cwts_training(models.Model):
    class_td = models.DateField(blank= True,null=True)
    td_count = models.CharField(max_length=254, default='')
    def __str__(self):
        return self.class_td
    
class Announcement(models.Model):
    assign = models.CharField(max_length=20, default='')
    subject = models.CharField(max_length=20, default='')
    content = models.CharField(max_length=500, default='')
    date_posted = models.DateTimeField(null=True, blank=True, default='')
    
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
    
class activity(models.Model):
    act_count = models.CharField(max_length=100, default='')
    act_title = models.CharField(max_length=100, default='')
    act_numbers = models.CharField(max_length=100, default='')
    
class midterm(models.Model):
    semester = models.CharField(max_length=20, default='')
    date = models.DateField(blank= True,null=True)
    items = models.CharField(max_length=100, default='')
    
    
class finals(models.Model):
    semester = models.CharField(max_length=20, default='')
    date = models.DateField(blank= True,null=True)
    items = models.CharField(max_length=100, default='')
    
class csv_attendance(models.Model):
    csvfile = models.FileField(upload_to='all_files/', default='')
    
# cwts grades

class cwts_grading(models.Model):
    attendance =  models.CharField(max_length=100, default='')
    quiz = models.CharField(max_length=100, default='')
    exercises = models.CharField(max_length=100, default='')
    midterm_exam = models.CharField(max_length=100, default='')
    final_exam =  models.CharField(max_length=100, default='')

    participation = models.CharField(max_length=100, default='')
    
    total = models.CharField(max_length=100, default='')
    
    
class cwts_activity(models.Model):
    act_count = models.CharField(max_length=100, default='')
    act_title = models.CharField(max_length=100, default='')
    act_numbers = models.CharField(max_length=100, default='')
    
    
class cwts_exercises(models.Model):
    act_count = models.CharField(max_length=100, default='')
    act_title = models.CharField(max_length=100, default='')
    act_numbers = models.CharField(max_length=100, default='')