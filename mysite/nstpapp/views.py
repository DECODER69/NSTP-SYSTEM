from dataclasses import field
import csv
from distutils.command.build_scripts import first_line_re
from genericpath import exists
from heapq import merge

from pkgutil import extend_path
from django.db.models import Sum
import re
# from subprocess import IDLE_PRIORITY_CLASS
from turtle import end_fill
from webbrowser import get
from django.http import HttpResponseRedirect
from django.http.request import QueryDict

from django.db.models import Count
from http.client import HTTPResponse
from django.urls import reverse
from multiprocessing import context
from pickle import FALSE
# from re import S
from tabnanny import check
from tkinter import FLAT
from urllib import response
from django.shortcuts import render, redirect,  reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
import datetime

#models imported
from .models import activity,cwts_certification,alumni_school_year,feedback, extenduser,school_year, sections, training_day,Announcement, certification, activity, midterm, finals, cwts_training, cwts_grading, cwts_activity, cwts_exercises, cwts_midterm, cwts_final, rfiles, cfiles
import os
import csv  

from django.db.models import Q



from django.http import HttpResponse, Http404

# emails
from django.core.mail import send_mail
from django.db import IntegrityError

# Create your views here.

# track active users
from django.utils.timezone import now
from datetime import timedelta
import datetime


import pandas as pd
#   PAGE SHOWING
def index(request):
    return render(request, 'activities/new_landing.html')
def signup_page(request):
    schools = school_year.objects.all()
    context = {
        'schools':[schools.last()],
    }
    return render(request, 'activities/signup.html', context)
def login_page(request):
    return render(request, 'activities/login.html')

@login_required(login_url='/login_page')
def dashboard_page(request):
    announcement = Announcement.objects.all().order_by('date_posted').reverse()
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    
    present2 = []
    absent2 = []
    name = extenduser.objects.filter(user = request.user)
    pres1 = extenduser.objects.filter(user = request.user)
    abs1 = extenduser.objects.filter(user = request.user)
    
    pres2 = extenduser.objects.filter(user = request.user)
    abs2 = extenduser.objects.filter(user = request.user)
    term = school_year.objects.all()
    
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    
    for s in pres2:
        present2.append(s.pres2)
       
    for k in abs2:
        absent2.append(k.abs2)

    context = {
        'name': name,
        'announcement': announcement,
        'present': present,
        'absent': absent,
        'labels': labels,
        'term':[term.last()],
        'present2': present2,
        'absent2': absent2,
        
      
    }
    print(labels)
    return render(request, 'activities/dashboard.html', context)

@login_required(login_url='/login_page')
def profile_page(request):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    
    present2 = []
    absent2 = []
    name = extenduser.objects.filter(user=request.user)
    pres1 = extenduser.objects.filter(user=request.user)
    abs1 = extenduser.objects.filter(user=request.user)
    pres2 = extenduser.objects.filter(user = request.user)
    abs2 = extenduser.objects.filter(user = request.user)
    section = sections.objects.all()
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(user=request.user)
    term = school_year.objects.all()
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
        
    for s in pres2:
        present2.append(s.pres2)
       
    for k in abs2:
        absent2.append(k.abs2)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'present2': present2,
        'absent2': absent2,
        'term':[term.last()],
    }
    
    return render(request, 'activities/profile.html', context)
@login_required(login_url='/login_page')
def editprofile(request):
    editwow = extenduser.objects.filter(user=request.user)
    context = {
        'ediwow':editwow,
    }
    return render(request, 'activities/editprofile.html', context)
@login_required(login_url='/login_page')
def others(request):
    uwu = extenduser.objects.filter(user=request.user)
    context = {
        'uwu':uwu,
    }
    return render(request, 'activities/others.html', context)
# @login_required(login_url='/login_page')
# def health(request):
#     uwus = extenduser.objects.filter(user=request.user)
#     context = {
#         'uwus':uwus,
#     }
#     return render(request, 'activities/health.html', context)

def file_manager(request):
    return render(request, 'activities/file_manager.html')

def files_rotc(request):
    return render(request, 'activities/files_rotc.html')
def files_cwts(request):
    return render(request, 'activities/files_cwts.html')
def fields(request):
    return render(request, 'activities/fields.html')

def field_rotc(request):
    return render(request, 'activities/field_rotc.html')



def admin_nav(request):
    pending = extenduser.objects.filter(status='PENDING').count()
    
    context = {
        'pending':pending,
        
    }
    return render(request, 'activities/admin_nav.html', context)
def navbar(request):
    return render(request, 'activities/navbar.html')
def logout_student(request):
    logout(request)
    return redirect('/login_page')

# ADMIN DISPLAY PAGE###################################
####################
#####################
####################
#########################
# ADMIN PAGE DISPLAYS
@login_required(login_url='/staff_signin')
def admin_dashboard(request):
    if request.user.is_staff:
        admin = User.objects.filter(is_superuser=True)
        staff = extenduser.objects.filter(user=request.user)
        feed = feedback.objects.filter(status = 'PENDING').order_by('date_sent')
        audience = sections.objects.all()
        ann = Announcement.objects.all()
        sy = school_year.objects.all()
        nav_pending_count = extenduser.objects.filter(status='PENDING').count()
        nav_rejected_count = extenduser.objects.filter(status='REJECTED').count()
        active = extenduser.objects.filter(status='ENROLLED').count()
        pending = extenduser.objects.filter(status='PENDING', category = 'STUDENT').count()

        context = {
            'active':active,   
            'pending':pending,
            'sy':[sy.last()],
            'audience':audience,
            'ann':ann,
            'staff':staff,
            'nav_pending_count':nav_pending_count,
            'nav_rejected_count':nav_rejected_count ,
            'feed':feed
        
        }
        return render(request, 'activities/admin_dashboard.html', context)
    return redirect('/')

def admin_staff(request):
    s_years = school_year.objects.all()
    details = extenduser.objects.filter(status='ENROLLED')
    pendings = extenduser.objects.filter(status='PENDING')
    pending = extenduser.objects.filter(status='PENDING').count()

    context = {
        'pending':pending,
        'details': details,
        'pendings':pendings,
        's_years':[s_years.last()]
       
    }
    
    return render(request, 'activities/admin_staffs.html', context)

def admin_pending(request):
    platoons = sections.objects.all()
    pending = extenduser.objects.filter(status='PENDING').filter(category = 'STUDENT').count()
    pendings = extenduser.objects.filter(status='PENDING').filter(category = 'STUDENT')

    context = {
        'pendings':pendings,
        'pending':pending,
        'platoons':platoons
    }
    return render(request, 'activities/admin_pending.html', context)


@login_required(login_url='/staff_signin')
def admin_rejected(request):
    # pending = extenduser.objects.filter(status='PENDING').count()
    if request.user.is_staff:
    
        rejected = extenduser.objects.filter(status='REJECTED').filter(field = 'ROTC')

        context = {
        
            'rejected':rejected,
        
        }
        return render(request, 'activities/admin_rejected.html', context)
    return redirect('/staff_signin')


@login_required(login_url='/staff_signin')
def cwts_admin_rejected(request):
    if request.user.is_staff:
    
    # pending = extenduser.objects.filter(status='PENDING').count()
        rejected = extenduser.objects.filter(status='REJECTED').filter(field = 'CWTS')

        context = {
        
            'rejected':rejected,
        
        }
        return render(request, 'activities/cwts_rejected.html', context)
    return redirect('/staff_signin')

def admin_view_profile(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    section =  sections.objects.filter(fiel = 'ROTC')
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id).filter(status='PENDING')
    
    sy = school_year.objects.all()
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1,
        'sy': [sy.last()]
    }
    

    
    return render(request, 'activities/profile_view.html', context)

def cwts_admin_view_profile(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    section = sections.objects.filter(fiel = 'CWTS')
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id).filter(status='PENDING')
    sy = school_year.objects.all()
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1,
        'sy': [sy.last()]
    }
    

    
    return render(request, 'activities/cwts_profile_view.html', context)
 

 



def create_platoon_page(request):
    current_datetime = datetime.datetime.now() 
    userContent = User.objects.all()
    sectionxx = extenduser.objects.all()
    counts = extenduser.objects.filter(status='ENROLLED').count()
    counts1 = extenduser.objects.filter(status='ENROLLED')
    section = sections.objects.all()
    section1 = sections.objects.all().count()
    context = {
        
    'counts':counts,
    'counts1':counts1,
    'section':section,
    'section1':section1,
    'sectionxx':sectionxx,
    'userContent':userContent,
    'current_datetime':current_datetime,
    }
    return render (request, 'activities/create_platoon.html', context)




def create_platoon_page2(request):
    sectionxx = extenduser.objects.all()
    counts = extenduser.objects.filter(status='ENROLLED').count()
    counts1 = extenduser.objects.filter(status='ENROLLED')
    section = sections.objects.all()
    section1 = sections.objects.all().count()
    context = {
        
    'counts':counts,
    'counts1':counts1,
    'section':section,
    'section1':section1,
    'sectionxx':sectionxx,
    }
    return render (request, 'activities/create_platoon2.html', context)


@login_required(login_url='/staff_signin')
def manage_section(request):
    if request.user.is_staff:
        current_datetime = datetime.datetime.now() 
        userContent = User.objects.all()
        sectionxx = extenduser.objects.all()
        counts = extenduser.objects.filter(status='ENROLLED').count()
        counts1 = extenduser.objects.filter(status='ENROLLED')
        section = sections.objects.filter(fiel='ROTC')
        section1 = sections.objects.all().count()
        secCount = request.POST.get('secCount')
        # counts3 = extenduser.objects.filter(status='ENROLLED').filter(platoons='ALPHA')
        context = {
            
        'counts':counts,
        'counts1':counts1,
        'section':section,
        'section1':section1,
        'sectionxx':sectionxx,
        'userContent':userContent,
        'current_datetime':current_datetime,
        # 'counts3':counts3
        }
    
        print(secCount)
        return render(request, 'activities/manage_section.html', context)
    return redirect('/staff_signin')
    






# MALI ITOOO

def attendance_main_page(request):
    return render(request, 'activities/attendance_main.html')


# eof mali




#   EOF PAGE SHOWING

# functions

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        middle = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber = request.POST.get('idnumber')
        password = request.POST.get('password1')
        picture = request.FILES['picture']
        s_year = request.POST.get('s_year')
        field = request.POST.get('field')
        date_joined = datetime.datetime.now()  
        
        if User.objects.filter(username=idnumber).exists():
            messages.error(request, 'ID Number ' + str (idnumber) + ' Already Exist !')
            return redirect('/signup_page')
        elif extenduser.objects.filter(email=email).exists():
            messages.error(request, 'Email ' + str (email) + ' Already Exist !')
            return redirect('/signup_page')
       
        else:
            user = User.objects.create_user(username=idnumber, password=password, email=email, first_name=firstname, last_name=lastname)
            datas = extenduser(s_year=s_year,firstname=firstname, middlename=middle, lastname=lastname, email=email, date_joined = date_joined,  idnumber=idnumber,picture=picture, category = 'STUDENT', field=field,user=user)
            datas.save()
            auth.login(request, user)
            messages.error(request, 'Account created successfully\nPlease Login and complete profile for verification. Thank you')
            return redirect('/login_page')
    else:
        return redirect('/')


# def signin(request):
#     if request.method == "POST":
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             if User.objects.filter(username=username).exists():
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     auth.login(request, user)
#                     return redirect('/dashboard_page')
#                 else:
#                     messages.error(request, 'Incorrect password')
#                     return redirect('/login_page')
#             else:
#                 messages.error(request, 'ID Number ' + str (username) + ' Does not exist !')
#                 return redirect('/login_page')
#     else:
#         messages.error(request, 'Invalid username or password !')
#         return redirect('/login_page')


def signin(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            usertype = User.objects.filter(username=username).filter(is_staff=1)
            if User.objects.filter(username=username).exists():
                if usertype:
                    print("gago")
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        return redirect('/admin_dashboard')
                    else:
                        messages.error(request, 'Incorrect password')
                        return redirect('/login_page')
                else:
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        auth.login(request, user)
                        return redirect('/dashboard_page')
                    else:
                        messages.error(request, 'Incorrect password')
                        return redirect('/login_page')
                    
                
                
                # user = authenticate(username=username, password=password)
                # if user is not None:
                #     auth.login(request, user)
                #     return redirect('/dashboard_page')
                # else:
                #     messages.error(request, 'Incorrect password')
                #     return redirect('/login_page')
            else:
                messages.error(request, 'ID Number ' + str (username) + ' Does not exist !')
                return redirect('/login_page')
    else:
        messages.error(request, 'Invalid username or password !')
        return redirect('/login_page')

@login_required(login_url='/login_page')
def edit(request, id):

    if request.method == 'POST':
        gender = request.POST.get('gender')
        section = request.POST.get('section')
        email = request.POST.get('email')
        age = request.POST.get('age')
        civil = request.POST.get('civil')
        cpnumber = request.POST.get('cpnumber')
        address = request.POST.get('address')
        birthday = request.POST.get('birthday')
        nfather = request.POST.get('nfather')
        foccupation = request.POST.get('foccupation')
        nmother = request.POST.get('nmother')
        moccupation = request.POST.get('moccupation')
        pcontact = request.POST.get('pcontact')
        nguardian  = request.POST.get('nguardian')
        goccupation = request.POST.get('goccupation')
        gcontact = request.POST.get('gcontact')
        
        extenduser.objects.filter(user=request.user).update(gender=gender, section=section, email=email, age=age, 
                                                            civil=civil, cpnumber=cpnumber, address=address, birthday=birthday,
                                                            nfather=nfather, foccupation=foccupation, nmother=nmother, moccupation=moccupation,
                                                            pcontact=pcontact, nguardian=nguardian, goccupation=goccupation, gcontact=gcontact,
                                            )
        
        # proof = extenduser.objects.get(id=id)
   
        # proof.proof = request.FILES['proof']
        # image_path = proof.proof.path
        # if os.path.exists(image_path):
        #     os.remove(image_path)
        # proof.save()
        # return render(request, 'activities/others.html')
        return redirect('/health')
    else:
        return redirect('/editprofile')
@login_required(login_url='/login_page')
def edit_others(request, id):
    hehe = extenduser.objects.get(id=id)
    if request.method == 'POST':
        hehe.idpic = request.FILES['studentid']
        image_path = hehe.idpic.path
        if os.path.exists(image_path):
            os.remove(image_path)
        hehe.save()
        return redirect('/health')
    return redirect('/others')



def rotc_files(request):
    users = extenduser.objects.filter(user=request.user).filter(field='ROTC')
    if users:
        return redirect('/files_rotc')
    else:
        messages.error(request, 'You Are not Enrolled here !')
        return redirect('/file_manager')
    
def cwts_files(request):
    users = extenduser.objects.filter(user=request.user).filter(field='CWTS')
    if users:
        return redirect('/files_cwts')
    else:
        messages.error(request, 'You Are not Enrolled here !')
        return redirect('/file_manager')




########################
############################
######################
#############

# ADMIN FUNCTIONS ################################

def approve(request, idnumber):
    stat2 = request.POST.get('getID')
    platoons = request.POST.get('platoons')
    

    extenduser.objects.filter(idnumber=stat2).update(status='ENROLLED', first_sem='ENROLLED')
    messages.success(request, 'Student ' + str (stat2) + ' has been Approved !')
    return redirect('/admin_pending')

def cw_approve(request, idnumber):
    stat2 = request.POST.get('getID')
    platoons = request.POST.get('platoons')
    

    extenduser.objects.filter(idnumber=stat2).update(status='ENROLLED', first_sem='ENROLLED')
    messages.success(request, 'Student ' + str (stat2) + ' has been Approved !')
    return redirect('/cwts_admin_pending')

def decline(request, id):
   
    stat2 = request.POST.get('getID2')
   
    print(stat2)
    extenduser.objects.filter(idnumber=stat2).update(status='REJECTED')
    messages.success(request, 'Student ' + str (stat2) + ' has been Rejected !')
    return redirect('/admin_pending')

def cw_decline(request, id):
       
    stat2 = request.POST.get('getID2')
   
    print(stat2)
    extenduser.objects.filter(idnumber=stat2).update(status='REJECTED')
    messages.success(request, 'Student ' + str (stat2) + ' has been Rejected !')
    return redirect('/cwts_admin_pending')

def r_approve(request, idnumber):
    stat2 = request.POST.get('getID')
 
    

    extenduser.objects.filter(idnumber=stat2).update(status='ENROLLED', platoons='PROCESSING', first_sem = 'ENROLLED')
    messages.success(request, 'Student ' + str (stat2) + ' has been Approved !')
    return redirect('/admin_rejected')

def r_decline(request, id):
    extenduser.objects.filter(id=id).delete()
    User.objects.filter(id=id).delete()
    return redirect('/admin_rejected')

def c_approve(request, idnumber):
    stat2 = request.POST.get('getID')
    extenduser.objects.filter(idnumber=stat2).update(status='ENROLLED', platoons='PROCESSING', first_sem = 'ENROLLED')
    messages.success(request, 'Student ' + str (stat2) + ' has been Approved !')
    return redirect('/cwts_admin_rejected')

def c_decline(request, id):
    extenduser.objects.filter(id=id).delete()
    User.objects.filter(id=id).delete()
    return redirect('/cwts_admin_rejected')

# EMAILS
def rejected_email_page(request, id):
    rejects = extenduser.objects.filter(status='REJECTED')
    ems = extenduser.objects.filter(id=id)
    context = {
        'rejects':rejects,
        'ems':ems
    }
    
    
    return render(request, 'activities/rejected_email.html', context)

def custom(request):
    if request.method == 'POST':
        try:
            sub = request.POST.get('emailtext')
            msg = request.POST.get('message')
            emaila = request.POST.get('cusemail')
            send_mail(sub, msg,'tupc.nstp@gmail.com',[emaila])
            return redirect('/admin_rejected')
        except ImportError:
            messages.success(request, 'Email Encountered some errors. Please Contact your Administrator')
    return redirect('/admin_rejected')
        


def allumni_content(request):
    if request.method == 'POST':
        getYear = request.POST.get('getYear')
        content = extenduser.objects.filter(s_year=getYear).filter(status='GRADUATE')
        content2 = extenduser.objects.filter(s_year=getYear).count()
    else:
        print("hahahahaaha")
        return render(request, 'activities/allumni_content.html')
    context = {
        'content':content,
        'content2':content2,
        'getYear':getYear,
    }
    print(getYear)


    return render(request, 'activities/allumni_content.html', context)




def delete_sy(request, years):
    school_year.objects.filter(years=years).delete()
    alumni_school_year.objects.filter(years=years).delete()
    print(id)
    return redirect('/school_years')

def create_section(request):
    if request.method == 'POST':
        secs = request.POST.get('secs')
        field = request.POST.get('field')
        if secs is not None and field is not None:
            if sections.objects.filter(section_created  = secs).exists():
                messages.info(request, 'Section ' + str (secs) + ' Already exist !')
                return redirect('/manage_section')
            else:
                data = sections(section_created=secs, fiel=field)
                data.save()
                messages.info(request, 'Section ' + str (secs) + ' Created !')
                return redirect('/manage_section')
        else:
            messages.info(request, 'Please Input Something!! Ex: ALPHA')
            return redirect('/manage_section')
    return redirect('/manage_section')
    
def create_cwts_section(request):
    if request.method == 'POST':
        secs = request.POST.get('secs')
        field = request.POST.get('field')
        if secs is not None and field is not None:
            if sections.objects.filter(section_created  = secs).exists():
                messages.info(request, 'Section ' + str (secs) + ' Already exist !')
                return redirect('/manage_cwts_section')
            else:
                data = sections(section_created=secs, fiel=field)
                data.save()
                messages.info(request, 'Section ' + str (secs) + ' Created !')
                return redirect('/manage_cwts_section')
        else:
            messages.info(request, 'Please Input Something!! Ex: ALPHA')
            return redirect('/manage_cwts_section')
    return redirect('/manage_cwts_section')


def counts(request, secton_created):
    data1 = extenduser.objects.all()
    if request.method == 'POST':
        
        get_section = request.POST.get('get_section')
        get_count = extenduser.objects.filter(platoons=get_section).filter(status='ENROLLED').count()
        context = {
            'get_count':get_count,
            'data1':data1
        }
        
        return redirect('/create_platoon_page', context)
    return redirect('/create_platoon_page', context)



def view_images(request, id):
    counts = extenduser.objects.filter(status='ENROLLED').count()
    counts1 = extenduser.objects.filter(status='ENROLLED')
    section = sections.objects.all()
    section1 = sections.objects.all().count()
    datas = extenduser.objects.filter(id=id)
    sectionxx = extenduser.objects.all()
    userContent = User.objects.all()
    context = {
        'datas':datas,
        'counts':counts,
        'counts1':counts1,
        'section':section,
        'section1':section1,
        'sectionxx':sectionxx,
        'userContent':userContent
    }

    return render(request, 'activities/create_platoon2.html', context)

def edit_manage(request, id):
    counts = extenduser.objects.filter(status='ENROLLED').count()
    counts1 = extenduser.objects.filter(status='ENROLLED')
    section = sections.objects.all()
    section1 = sections.objects.all().count()
    datas = extenduser.objects.filter(id=id)
    sectionxx = extenduser.objects.all()
    userContent = User.objects.all()
    context = {
        'datas':datas,
        'counts':counts,
        'counts1':counts1,
        'section':section,
        'section1':section1,
        'sectionxx':sectionxx,
        'userContent':userContent
    }
    if request.method == 'POST':
        try:
            id= request.POST.get('ids')
            sub = request.POST.get('emailtext')
            msg = request.POST.get('message')
            emaila = request.POST.get('rname')
            send_mail(sub, msg,'tupc.nstp@gmail.com',[emaila])
            messages.success(request, 'Email Sent to ' +str(emaila))
            
        except ImportError:
            messages.success(request, 'Email Encountered some errors. Please Contact your Administrator')

    return render (request, 'activities/edit_manage.html', context)

def update_manage(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        address = request.POST.get('address')
        cpnumber = request.POST.get('cpnumber')
        birthday = request.POST.get('birthday')
        age = request.POST.get('age')
        civil = request.POST.get('civil')
        email = request.POST.get('email')
        idnumber = request.POST.get('idnumber')
        status =request.POST.get('status')
        field = request.POST.get('field')
        platoons = request.POST.get('platoons')
        section2 = request.POST.get('section')
        nfather = request.POST.get('nfather')
        foccupation = request.POST.get('foccupation')
        nmother = request.POST.get('nmother')
        moccupation  = request.POST.get('moccupation')
        pcontact = request.POST.get('pcontact')
        nguardian = request.POST.get('nguardian')
        goccupation = request.POST.get('goccupation')
        gcontact = request.POST.get('gcontact')
        
        extenduser.objects.filter(id=ids).update(firstname = firstname, middlename = middlename, lastname = lastname, 
                                                 address = address, cpnumber=cpnumber, birthday=birthday, age=age,
                                                 civil=civil,email=email,idnumber=idnumber,status=status,field=field,
                                                 platoons=platoons, section=section2,nfather=nfather, foccupation=foccupation, nmother=nmother, moccupation=moccupation,
                                                 pcontact=pcontact, nguardian=nguardian, goccupation=goccupation, gcontact=gcontact)
        User.objects.filter(id=ids).update(username=idnumber)
        messages.success(request, str(idnumber)+' has been Updated')
        return redirect('/create_platoon_page')

    return redirect('/create_platoon_page')
        
        
        
    


def export(request):
    normal_style = xlwt.easyxf("""
     font:
         name Verdana
     """) 
    response = HTTPResponse(content_type='application/ms-excel')
    wb = xlwt.Workbook()
    ws0 = wb.add_sheet('Worksheet')
    ws0.write(0, 0, "something", normal_style)
    wb.save(response)
    return response

def edit_student(request, id):
    idnums = request.POST.get('geti')

    firstname = request.POST.get('firstname')
    middle = request.POST.get('middle')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    idnumber = request.POST.get('idnumber')
    gender = request.POST.get('gender')
    address = request.POST.get('address')
    cpnumber = request.POST.get('cpnumber')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    section = request.POST.get('section')
    civil = request.POST.get('civil')
    nfather = request.POST.get('nfather')
    foccupation  =request.POST.get('foccupation')
    pcontact = request.POST.get('pcontact')
    nmother = request.POST.get('nmother')
    moccupation  =request.POST.get('moccupation')
    pcontact = request.POST.get('pcontact')
    disease = request.POST.get('disease')
    specific = request.POST.get('specific')
    
    extenduser.objects.filter(id=idnums).update(firstname=firstname, middlename = middle, 
                                                lastname=lastname, email=email, idnumber=idnumber, gender=gender,
                                                address=address, cpnumber=cpnumber, birthday=birthday, age=age, 
                                                section=section, civil=civil, nfather=nfather, foccupation=foccupation,
                                                pcontact=pcontact, nmother=nmother, moccupation=moccupation, disease=disease, specific=specific)

    return redirect('/create_platoon_page')
    
    


@login_required(login_url='/staff_signin')
def section_content(request):
    if request.user.is_staff:
    
        userContent = User.objects.all()
        schools = school_year.objects.all()
        rotc_section = sections.objects.filter(fiel='ROTC')
        if request.method == 'POST':
        
            getSection = request.POST.get('getSection')
            print(getSection)
            content3 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
            content33 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED').count()
        else:
        
            return render(request, 'activities/pl_content.html')
        context = {
            'content3':content3,
            'userContent':userContent,
            'content33':content33,
            'getSection':getSection,
            'schools':[schools.last()],
            'section':rotc_section
            
        }
        print(content33)
        print(getSection)
        return render(request, 'activities/pl_content.html', context)
    return redirect('/staff_signin')


# TO BE CONTINUED AFTER DEFENSE
def download(request):
    if request.method == 'POST':
    
        csvfile = extenduser.objects.filter(status='ENROLLED')
        response = HttpResponse(content_type='text/csv')  
        print("CSV FILE ITO" + str(csvfile))
        
        response['Content-Disposition'] = 'attachment; filename="List.csv"  '
        writer = csv.writer(response)  
        writer.writerow(['ATTENDANCE 30%', 'MERITS 30%', 'ACTIVITIES 10%', 'MIDTERM EXAM 15%', 'FINAL EXAM 15%', 'FINAL GRADE'])  
        for s in csvfile:  
   
            writer.writerow([s.idnumber, s.firstname, s.lastname, s.field, s.platoons, s.status])  
    return response  
def download1(request):
    if request.method == 'POST':
    
        csvfile = extenduser.objects.filter(status='ENROLLED')
        response = HttpResponse(content_type='text/csv')  
        print("CSV FILE ITO" + str(csvfile))
        
        response['Content-Disposition'] = 'attachment; filename="Student list.csv"  '
        writer = csv.writer(response)  
        writer.writerow(['STUDENT NUMBER', 'FIRSTNAME', 'LASTNAME', 'NSTP COMPONENT', 'NSTP SECTION'])  
        for s in csvfile:  
   
            writer.writerow([s.idnumber, s.firstname, s.lastname, s.field, s.platoons])  
    return response  



def create_day(request):
    if request.method == 'POST':
   
        title = request.POST.get('title')
        if training_day.objects .filter(title=title).exists():
            messages.info(request, (title) + ' Already exist !')
            return redirect('/attendance_page')

        else:
            data = training_day( title=title)
            data.save()
            messages.info(request, (title) + ' Created !')
            return redirect('/attendance_page')

    return redirect('/attendance_page')

def section_day(request):
    return redirect('/attendance_page')

def create_announcement(request):
    date = datetime.datetime.now()  
    if request.method == 'POST':
        assign = request.POST.get('assign')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        context = {
            'assign':assign
        }
        
        alls = Announcement(assign=assign, subject=subject, content=content, date_posted=date)
        alls.save()
        messages.info(request, 'Announcement ' + str(subject + ' has been posted.'))
        return redirect('/admin_dashboard', context)
    return redirect('/admin_dashboard')

def edit_announcement(request, id):
    if request.method == 'POST':
        ID = request.POST.get('ID')
        content = request.POST.get('content')
        Announcement.objects.filter(id=ID).update(content=content)
        # messages.info(request, 'Edit Success')
        return redirect('/admin_dashboard')
    return redirect('/admin_dashboard')
def delete_announcement(request, id):
    Announcement.objects.filter(id=id).delete()
  
    return redirect('/admin_dashboard')

# for attendance only
     
def attendance_page(request):
    platoons = sections.objects.all()
    days = training_day.objects.all()
    day_count = training_day.objects.all().count()
    context = {
        'days':days,
        'day_count':day_count,
        'platoons':platoons
    }
    return render(request, 'activities/attendance_page.html', context)

def attendance_sections(request):
    platoons = sections.objects.all()
  
    t_days = request.POST.get('t_day')
    he = training_day.objects.filter(title=t_days)


    context = {
        'platoons':platoons,
        'he':he
    }
    return render(request, 'activities/attendance_section.html', context)

# def attendance_main_page(request):
#     return render(request, 'activities/attendance_main.html', context)


def attendance_main(request):
    schools = school_year.objects.all()
    counts = 3

    if request.method == 'POST':
        getSection = request.POST.get('getSection')
        # t_day = request.POST.get('t_day')
        # print("pogi ako talaga  " +str( t_day))
        
        sectionx = sections.objects.all()
        content3 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        content33 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED').count()
        # messages.info(request, 'Attendance Up to date')

    else:
        return redirect('/attendance_sections')
    context = {
        'content3':content3,
        'content33':content33,
        'getSection':getSection,
        'schools':[schools.last()],
        'sectionx':sectionx,
        'counts':counts
        # 't_day':t_day
       
    }
    return render(request, 'activities/attendance_main.html', context)
  






    # return HttpResponseRedirect(request.session['getSection1'])

def pl_content(request):
    return render(request, 'activities/pl_content.html')


@login_required(login_url='/staff_signin')
def add_students(request):
    if request.user.is_staff:
        if request.method == 'POST':
            platoon = request.POST.get('platoon')
            allstudent = extenduser.objects.filter(status='ENROLLED').filter(platoons='PROCESSING').filter(field='ROTC')
        else:
            return redirect('/manage_section')
        context = {
            'allstudent':allstudent,
            'platoon':platoon
        }
        return render(request, 'activities/students_list.html', context)
    return redirect('/staff_signin')
def assign_section(request):
    if request.method == 'POST':
        platoons=request.POST.get('platoons')
        lists = request.POST.getlist('students[]')
 
        for s in lists:
            extenduser.objects.filter(id=s).update(platoons=platoons)
            print("id ito" +str(s))
            messages.info(request, 'Adding Students to ' + str(platoons + ' done.'))

        messages.info(request, 'Adding Students to ' + str(platoons + ' done.'))
        print("tanga")
        return redirect('/manage_section')
    else:
        return redirect('/manage_section')

def update_sy(request, ):
    if request.method == 'POST':
        status = request.POST.get('status')
        current = request.POST.get('current')
        school_year.objects.filter(id=current).update(sem=status)
        print("School year status Updated")
    return redirect('/school_years')


def update_sys(request, ):
    if request.method == 'POST':
        status = request.POST.get('status_sys')
        current = request.POST.get('current')
        school_year.objects.filter(id=current).update(status=status)
        print("School year status Updated")
    return redirect('/school_years')

def update_officially(request, id):
    if request.method == 'POST':
        stats = request.POST.get('slc')
        idd = request.POST.get('idd')
        print("hahaha" +str(idd))
        extenduser.objects.filter(id=idd).update(status=stats)
    return redirect('/admin_staff')

def cert_page(request):
    sys = school_year.objects.all()
    pota = extenduser.objects.filter(status='ENROLLED')
  
    # last = school_year.objects.all()
    details = certification.objects.all()
    context = {
        'sys':sys,
        'details':[details.last()],
        'pota':pota,
        # 'last':[last.last()],
    }
    return render(request, 'activities/rotc_cert_page.html', context)


def cwts_cert_page(request):
    sys = school_year.objects.all()
    pota = extenduser.objects.filter(status='ENROLLED')
    # last = school_year.objects.all()
    details = cwts_certification.objects.all()
    context = {
        'sys':sys,
        'details':[details.last()],
        'pota':pota,
        # 'last':[last.last()],
    }
    return render(request, 'activities/cwts_cert_page.html', context)
    # return render(request, 'activities/certificate_page.html', context)

def open_cert_page(request):
    section = sections.objects.all()
    if request.method == 'POST':
        sy = request.POST.get('years')
        bracket = extenduser.objects.filter(s_year=sy)
        sen5 = school_year.objects.filter(years=sy)

        context = {
            'bracket':bracket,
            'section':section,
            'sen5':sen5
         
        }
    
    return render(request, 'activities/cert_section.html', context)

def generate(request):
    
    if request.method == 'POST':
        years = request.POST.get('years')
        sys1 = school_year.objects.filter(years=years)
        section = request.POST.get('section')
        details = certification.objects.all()
        
        yyy =  extenduser.objects.filter(s_year=years).filter(status='GRADUATE')
        namess = extenduser.objects.filter(s_year=years).filter(status='GRADUATE').filter(field='ROTC')
        print(section)
        print("pogi"+str(years))
        
        context = {
            'yyy':yyy,
            'sys1':sys1,
            'namess':namess,
            'details':[details.last()],
            
        }
        return render(request, 'activities/certificate.html', context)
    
def cwts_generate(request):
    
    if request.method == 'POST':
        years = request.POST.get('years')
        sys1 = school_year.objects.filter(years=years)
        section = request.POST.get('section')
        details = certification.objects.all()
        yyy =  extenduser.objects.filter(s_year=years).filter(status='GRADUATE')
        namess = extenduser.objects.filter(s_year=years).filter(status='GRADUATE').filter(field='CWTS')
        print(section)
        print("pogi"+str(years))
        
        context = {
            'yyy':yyy,
            'sys1':sys1,
            'namess':namess,
            'details':[details.last()],
            
        }
        return render(request, 'activities/cwts_certificate.html', context)
    
def add_details(request):
    if request.method == 'POST':
        sys1 = request.POST.get('sys1')
        commandant = request.POST.get('commandant')
        registrar = request.POST.get('registrar')
        month = request.POST.get('month')
        date = request.POST.get('date')
        year = request.POST.get('year')
        data = certification(school_year2=sys1, commandant=commandant, registrar=registrar, month=month, date=date, year=year)
        data.save()
    return redirect('/cert_page', context)

def cwts_add_details(request):
    if request.method == 'POST':
        sys1 = request.POST.get('sys1')
        commandant = request.POST.get('commandant')
        registrar = request.POST.get('registrar')
        month = request.POST.get('month')
        date = request.POST.get('date')
        year = request.POST.get('year')
        data = cwts_certification(school_year2=sys1, commandant=commandant, registrar=registrar, month=month, date=date, year=year)
        data.save()
    return redirect('/cwts_cert_page', context)

def update_acts(request):
    if request.method == 'POST':
        current_datetime = datetime.datetime.now() 
        generate_by = request.POST.get('generate_by')
        ids= request.POST.get('ids')
        print("acts" + str(ids))
        school_year.objects.filter(years=ids).update(acts='DONE', date_generated=current_datetime, generate_by=generate_by)
        print("acts" + str(ids))
        return redirect('/cert_page')
    
def cwts_update_acts(request):
    if request.method == 'POST':
        generate_by = request.POST.get('generate_by')
        current_datetime = datetime.datetime.now() 
        ids= request.POST.get('ids')
        print("hahahaha" + str(ids))
        school_year.objects.filter(years=ids).update(acts_2='DONE', date_generated_2=current_datetime, generate_by2=generate_by)
        print("hahahaha" + str(ids))
        return redirect('/cwts_cert_page')
        
def admin_files(request):
    section = sections.objects.all()
    context = {
        'section':section
    }
    return render(request, 'activities/admin_files.html', context)

def open_folder(request,section_created):
   
    getSection = request.POST.get('getSection')
    print("hahahahahahaha" +str(getSection))
    context = {
    'getSection':getSection
    }

    return render(request, 'activities/open_folder.html', context)

def dropped(request):
    current_datetime = datetime.datetime.now() 
    userContent = User.objects.all()
    sectionxx = extenduser.objects.all()
    counts = extenduser.objects.filter(status='DROPPED').count()
    counts1 = extenduser.objects.filter(status='DROPPED')
    section = sections.objects.all()
    section1 = sections.objects.all().count()
    context = {
        
    'counts':counts,
    'counts1':counts1,
    'section':section,
    'section1':section1,
    'sectionxx':sectionxx,
    'userContent':userContent,
    'current_datetime':current_datetime,
    }
    return render (request, 'activities/dropped.html', context)

def download3(request):
    if request.method == 'POST':
    
        csvfile = extenduser.objects.filter(status='DROPPED')
        response = HttpResponse(content_type='text/csv')  
        print("CSV FILE ITO" + str(csvfile))
        
        response['Content-Disposition'] = 'attachment; filename="Drop list.csv"  '
        writer = csv.writer(response)  
        writer.writerow(['STUDENT NUMBER', 'FIRSTNAME', 'LASTNAME', 'NSTP COMPONENT', 'NSTP SECTION', 'STATUS'])  
        for s in csvfile:  
   
            writer.writerow([s.idnumber, s.firstname, s.lastname, s.field, s.platoons, s.status])  
    return response  



def download4(request):
    if request.method == 'POST':
        getSection = request.POST.get('cate')
        csvfile = extenduser.objects.filter(status='ENROLLED').filter(platoons=getSection)
        response = HttpResponse(content_type='text/csv')  
        print("CSV FILE ITO" + str(csvfile))
        
        response['Content-Disposition'] = 'attachment; filename="Attendance.csv"  '
        writer = csv.writer(response)  
        writer.writerow(['STUDENT NUMBER', 'FIRSTNAME', 'LASTNAME', 'SIGNATURE', 'REMARKS'])  
        for s in csvfile:  
   
            writer.writerow([s.idnumber, s.firstname, s.lastname])  
    return response  

@login_required(login_url='/staff_signin')
def sample_attendance(request):
    if request.user.is_staff:
        section = sections.objects.all()
        date = training_day.objects.all()

        context = {
            'date':date, 
            'section':section,
        }

        return render(request, 'activities/sample_attendance.html', context)
    return redirect('/staff_signin')

@login_required(login_url='/staff_signin')
def show_students(request):
    if request.user.is_staff:
        counted = training_day.objects.values_list('td_count', flat=True).count()
        getSection = request.POST.get('getSection')
        content3 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        content33 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED').count()
        context = {
            'content3':content3,
            'getSection':getSection,
            'counted':counted,
            'content33':content33,
        }
        return render(request, 'activities/show_studens.html', context)
    return redirect('/staff_signin')

def create_td(request):
    if request.method == 'POST':
        td = request.POST.get('td')
        td_count = request.POST.get('td_count')
        if training_day.objects.filter(td=td).exists():
            messages.error(request, 'Training Day already exists ' +str(td))
            return redirect('/sample_attendance')
        elif training_day.objects.filter(td_count =td_count).exists():
            messages.error(request, 'Training Day count exists ' +str(td_count))
            return redirect('/sample_attendance')
        else:
            alls = training_day(td=td, td_count=td_count)
            alls.save()
            return redirect('/sample_attendance')
    return redirect('/sample_attendance')
def create_td2(request):
    if request.method == 'POST':
        td = request.POST.get('td')
        td_count = request.POST.get('td_count')
        if training_day.objects.filter(td=td).exists():
            messages.error(request, 'Training Day already exists ' +str(td))
            return redirect('/attendance_tab')
        elif training_day.objects.filter(td_count =td_count).exists():
            messages.error(request, 'Training Day count exists ' +str(td_count))
            return redirect('/attendance_tab')
        else:
            alls = training_day(td=td, td_count=td_count)
            alls.save()
            return redirect('/attendance_tab')
    return redirect('/attendance_tab')

def open_date(request):
    section = sections.objects.filter(fiel = 'ROTC')
    if request.method == 'POST':
        td_count = request.POST.get('td_count')
        date = request.POST.get('date')
        context = {
            'date':date,
            'section':section,
            'td_count':td_count
        }
        return render(request, 'activities/open_date.html', context)
    return render(request, 'activities/open_date.html')

def all_sections(request):
    all_section = sections.objects.all()
    date = training_day.objects.all()
    td_count = training_day.objects.all()
    td_counts = request.POST.get('td_counts')
    print("counts " +str(td_counts))
    context = {
        'all_section':all_section,
        'date':[date.last()],
        'td_count':[td_count.last()],
        'td_counts':td_counts
    }
    return render(request, 'activities/all_sections.html', context)

def open_sections(request):
    if request.method == 'POST':
        td_count = request.POST.get('td_count')
        date0 = request.POST.get('date')
        date1 = request.POST.get('date1')
        getSection = request.POST.get('getSection')

        student = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        counts =  extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED').count()
        print(getSection)
        print(date0)
        print(date1)
        context = {
            'date0':date0,
            'getSection':getSection,
            'student':student,
            'counts':counts,
            'date1':date1,
            'td_count':td_count
          
        }
 
        return render(request, 'activities/open_sections.html', context)
    return render(request, 'activities/open_sections.html')
    
def del_tday(request, id):

    training_day.objects.filter(id=id).delete()
    return redirect('/sample_attendance')

def download5(request):
    if request.method == 'POST':
        getSection = request.POST.get('cate')
        csvfile = extenduser.objects.filter(status='ENROLLED').filter(platoons=getSection)
        response = HttpResponse(content_type='text/csv')  
        print("CSV FILE ITO" + str(csvfile))
        
        response['Content-Disposition'] = 'attachment; filename="Attendance.csv"  '
        writer = csv.writer(response)  
        writer.writerow(['STUDENT NUMBER', 'FIRSTNAME', 'LASTNAME', 'SIGNATURE', 'REMARKS'])  
        for s in csvfile:  
   
            writer.writerow([s.idnumber, s.firstname, s.lastname])  
    return response  

def rec_attendance(request):
    if request.method == 'POST':
        demerits = request.POST.getlist('quantity')
        mer_id = request.POST.getlist('mer_id')
        td_count = request.POST.get('td_count')
        
        ids = request.POST.getlist('id4')
        id2 = request.POST.getlist('id2')
        
        
        ids_2 = request.POST.getlist('ids_2')
        id4_2 = request.POST.getlist('id4_2')
        
        mer2_id = request.POST.getlist('mer2_id')
        demerits2 = request.POST.getlist('demerits2')
        
        if td_count == str(1):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD1_dem=t, first_merits=t)
        elif td_count == str(2):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD2_dem=t, first_merits=t)
        elif td_count == str(3):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD3_dem=t, first_merits=t)
        elif td_count == str(4):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD4_dem=t, first_merits=t)
        elif td_count == str(5):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD5_dem=t, first_merits=t)
        elif td_count == str(6):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD6_dem=t, first_merits=t)
        elif td_count == str(7):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD7_dem=t, first_merits=t)
        elif td_count == str(8):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD8_dem=t, first_merits=t)
        elif td_count == str(9):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD9_dem=t, first_merits=t)
        elif td_count == str(10):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD10_dem=t, first_merits=t)
        elif td_count == str(11):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD11_dem=t, first_merits=t)
        elif td_count == str(12):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD12_dem=t, first_merits=t)
        elif td_count == str(13):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD13_dem=t, first_merits=t)  
        elif td_count == str(14):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD14_dem=t, first_merits=t)
        elif td_count == str(15):
            for s, t in zip(mer_id, demerits):
                extenduser.objects.filter(id=s).update(TD15_dem=t, first_merits=t)
                


                
        if td_count == str(1):
            if ids:
                for i in ids:
                    print("present date 0 ff "+str(i))
                    extenduser.objects.filter(id=i).update(TD1='1')
            if id2:
                for j  in  id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD1='0')
                
        elif td_count == str(2):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD2='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD2='0')
        elif td_count == str(3):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD3='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD3='0')
        elif td_count == str(4):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD4='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD4='0')
        elif td_count == str(5):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD5='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD5='0')
        elif td_count == str(6):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD6='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD6='0')
        elif td_count == str(7):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD7='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD7='0')
        elif td_count == str(8):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD8='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD8='0')
        elif td_count == str(9):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD9='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD9='0')
        elif td_count == str(10):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD10='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD10='0')
        elif td_count == str(11):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD11='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD11='0')
        elif td_count == str(12):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD12='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD12='0')
        elif td_count == str(13):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD13='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD13='0')
        elif td_count == str(14):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD14='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD14='0')
        elif td_count == str(15):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD15='1')
            if id2:
                for j in id2:
                    print("absent date 0 "+str(j))
                    extenduser.objects.filter(id=j).update(TD15='0')
                    
                    
# FOR 2ND SEM merits

        if td_count == str(1):
            if ids_2:
                for i in ids_2:
                    print("present 2nd sem" + str(i))
                    extenduser.objects.filter(id=i).update(TD1_2='1')
            if id4_2:
                for i in id4_2:
                    print("absent 2nd sem" + str(i))
                    extenduser.objects.filter(id=i).update(TD1_2='0')
            
        if td_count == str(2):
            if ids_2:
                for i in ids_2:
                    print("present 2nd sem" + str(i))
                    extenduser.objects.filter(id=i).update(TD2_2='1')
            if id4_2:
                for i in id4_2:
                    print("absent 2nd sem" + str(i))
                    extenduser.objects.filter(id=i).update(TD2_2='0')
                    
        if td_count == str(3):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD3_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD3_2='0')
        if td_count == str(4):
            if ids_2:
                for i in ids_2:
                    print("present td 4")
                    extenduser.objects.filter(id=i).update(TD4_2='1')
            if id4_2:
                for i in id4_2:
                    print("absent td4" +str(i))
                    extenduser.objects.filter(id=i).update(TD4_2='0')
        if td_count == str(5):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD5_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD5_2='0')
        if td_count == str(6):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD6_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD6_2='0')
        if td_count == str(7):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD7_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD7_2='0')
        if td_count == str(8):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD8_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD8_2='0')
        if td_count == str(9):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD9_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD9_2='0')
        if td_count == str(10):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD10_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD10_2='0')                    
        if td_count == str(11):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD11_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD11_2='0')                   
        if td_count == str(12):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD12_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD12_2='0')                    
        if td_count == str(13):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD13_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD13_2='0')
        if td_count == str(14):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD14_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD14_2='0')
                    
        if td_count == str(15):
            if ids_2:
                for i in ids_2:
                    extenduser.objects.filter(id=i).update(TD15_2='1')
            if id4_2:
                for i in id4_2:
                    extenduser.objects.filter(id=i).update(TD15_2='0')
            
            # for 2nd sem merits
            
            
    return redirect('/sample_attendance', context)







def update_attendance(request):
    if request.method == 'POST':
        # presents
        td1 = request.POST.getlist('td1[]')
        td2 = request.POST.getlist('td2[]')
        td3 = request.POST.getlist('td3[]')
        td4 = request.POST.getlist('td4[]')
        td5 = request.POST.getlist('td5[]')
        td6 = request.POST.getlist('td6[]')
        td7 = request.POST.getlist('td7[]')
        td8 = request.POST.getlist('td8[]')
        td9 = request.POST.getlist('td9[]')
        td10 = request.POST.getlist('td10[]')
        td11 = request.POST.getlist('td11[]')
        td12 = request.POST.getlist('td12[]')
        td13 = request.POST.getlist('td13[]')
        td14 = request.POST.getlist('td14[]')
        td15 = request.POST.getlist('td15[]')
        
        # ABSENTS
        td1A = request.POST.getlist('td1A[]')
        td2A = request.POST.getlist('td2A[]')
        td3A = request.POST.getlist('td3A[]')
        td4A = request.POST.getlist('td4A[]')
        td5A = request.POST.getlist('td5A[]')
        td6A = request.POST.getlist('td6A[]')
        td7A = request.POST.getlist('td7A[]')
        td8A = request.POST.getlist('td8A[]')
        td9A = request.POST.getlist('td9A[]')
        td10A = request.POST.getlist('td10A[]')
        td11A = request.POST.getlist('td11A[]')
        td12A = request.POST.getlist('td12A[]')
        td13A = request.POST.getlist('td13A[]')
        td14A = request.POST.getlist('td14A[]')
        td15A = request.POST.getlist('td15A[]')

        for s in td1:
            extenduser.objects.filter(id=s).update(TD1='PRESENT')
            print(s)
        
        for s in td2:
            extenduser.objects.filter(id=s).update(TD2='PRESENT')
            print(s)
        
        for s in td3:
            extenduser.objects.filter(id=s).update(TD3='PRESENT')
        for s in td4:
            extenduser.objects.filter(id=s).update(TD4='PRESENT')
        for s in td5:
            extenduser.objects.filter(id=s).update(TD5='PRESENT')
        for s in td6:
            extenduser.objects.filter(id=s).update(TD6='PRESENT')

        for s in td7:
            extenduser.objects.filter(id=s).update(TD7='PRESENT')
        for s in td8:
            extenduser.objects.filter(id=s).update(TD8='PRESENT')
        for s in td9:
            extenduser.objects.filter(id=s).update(TD9='PRESENT')
        for s in td10:
            extenduser.objects.filter(id=s).update(TD10='PRESENT')
        for s in td11:
            extenduser.objects.filter(id=s).update(TD11='PRESENT')
        for s in td12:
            extenduser.objects.filter(id=s).update(TD12='PRESENT')
        for s in td13:
            extenduser.objects.filter(id=s).update(TD13='PRESENT')
        for s in td14:
            extenduser.objects.filter(id=s).update(TD14='PRESENT')
        for s in td15:
            extenduser.objects.filter(id=s).update(TD15='PRESENT')
            
            # ABSENNNNNNNNT
        for a in td1A:
            extenduser.objects.filter(id=a).update(TD1='ABSENT')
        for a in td2A:
            extenduser.objects.filter(id=a).update(TD2='ABSENT')
        for a in td3A:
            extenduser.objects.filter(id=a).update(TD3='ABSENT')
        for a in td4A:
            extenduser.objects.filter(id=a).update(TD4='ABSENT')
        for a in td5A:
            extenduser.objects.filter(id=a).update(TD5='ABSENT')
        for a in td6A:
            extenduser.objects.filter(id=a).update(TD6='ABSENT')
        for a in td7A:
            extenduser.objects.filter(id=a).update(TD7='ABSENT')
        for a in td8A:
            extenduser.objects.filter(id=a).update(TD8='ABSENT')
        for a in td9A:
            extenduser.objects.filter(id=a).update(TD9='ABSENT')
        for a in td10A:
            extenduser.objects.filter(id=a).update(TD10='ABSENT')
        for a in td11A:
            extenduser.objects.filter(id=a).update(TD11='ABSENT')
        for a in td12A:
            extenduser.objects.filter(id=a).update(TD12='ABSENT')
        for a in td13A:
            extenduser.objects.filter(id=a).update(TD13='ABSENT')
        for a in td14A:
            extenduser.objects.filter(id=a).update(TD14='ABSENT')
        for a in td15A:
            extenduser.objects.filter(id=a).update(TD15='ABSENT')
   
        messages.info(request, 'Attendance Up to date')
    return redirect('/attendance_page')

def update_att_credits(request):
    if request.method == 'POST':
        pres1 = request.POST.getlist('pres1')
        abs1 = request.POST.getlist('abs1')
        pres2 = request.POST.getlist('pres2')
        abs2 = request.POST.getlist('abs2')
        percentages = request.POST.getlist('percentage')
        percentages2 = request.POST.getlist('percentage2')
      

        ids = request.POST.getlist('getId')
        credits = request.POST.getlist('credits')
        ids2 = request.POST.getlist('ids2')
        credits2 = request.POST.getlist('credits2')
        print("creds "+ str(credits2))
        print("ids"+ str(ids2))
        
        for i, j, k, l, m in zip(ids, credits, pres1, abs1, percentages):
            extenduser.objects.filter(id=i).update(att_credits=j, pres1=k, abs1=l, percentage1=m)
        # extenduser.objects.filter
 
        
        for k, l, m, n, o in zip(ids2, credits2, pres2, abs2, percentages2):
            extenduser.objects.filter(id=k).update(att_credits_2=l, pres2=m, abs2=n, percentage2=o)
    return redirect('/attendance_tab')

@login_required(login_url='/staff_signin')
def grades(request):
    if request.user.is_staff:
        acts = activity.objects.all()
        section = sections.objects.filter(fiel= 'ROTC')
        context = {
            'section':section, 
            'acts': acts
        }
        return render(request, 'activities/grades.html', context)
    return redirect('/staff_signin')

@login_required(login_url='/staff_signin')
def modify_grades(request):
    if request.user.is_staff:
        total = activity.objects.aggregate(TOTAL = Sum('act_numbers'))['TOTAL']
        items = activity.objects.all()
        if request.method == 'POST':
            getSection = request.POST.get('getSection')
            content3 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
            context = {
                'content3':content3,
                'getSection':getSection,
                'total':total,
                'items':items
            }
            return render(request, 'activities/modify.html', context)
        return render(request, 'activities/modify.html', context)
    return redirect('/staff_signin')


def set_activities(request):
  
    if request.method == 'POST':
        title = request.POST.get('title')
        count = request.POST.get('count')
        numbers = request.POST.get('numbers')
        print(title, count, numbers)
        if activity.objects.filter(act_count=numbers).exists():
            messages.error(request, 'Training Day already exists ' )
        else:
            data = activity(act_title=title,act_count=numbers,  act_numbers=count)
            data.save()
    return redirect('/grades')


def save_grade(request):
    if request.method == 'POST':
        ids= request.POST.getlist('ids')
        
        credits1 = request.POST.getlist('credits1')
        credits2 = request.POST.getlist('credits2')
        print(ids)
        act1 = request.POST.getlist('act1')
        act2 = request.POST.getlist('act2')
        act3 = request.POST.getlist('act3')
        act4 = request.POST.getlist('act4')
        act5 = request.POST.getlist('act5')
        act6 = request.POST.getlist('act6')
        
        ids_2= request.POST.getlist('ids_2')
        act1_2 = request.POST.getlist('act1_2')
        act2_2 = request.POST.getlist('act2_2')
        act3_2 = request.POST.getlist('act3_2')
        act4_2 = request.POST.getlist('act4_2')
        act5_2 = request.POST.getlist('act5_2')
        act6_2 = request.POST.getlist('act6_2')
        # for a2 in (act1_2):
        for a, b, c, d , e, f , i, j in zip(act1, act2, act3, act4, act5, act6,  ids, credits1 ):
            extenduser.objects.filter(id=i).update(act1=a, act2=b, act3=c,act4=d, act5=e, act6=f, act_credits=j )
            print("hahaha "+ a, b, c, d , e, f)
            messages.success(request,'Updated')
            
        for a2, b2, c2, d2 , e2, f2, i2, j2 in zip( act1_2, act2_2, act3_2, act4_2, act5_2, act6_2,  ids_2, credits2):
            extenduser.objects.filter(id=i2).update(act1_2=a2, act2_2=b2, act3_2=c2, act4_2=d2, act5_2=e2, act6_2=f2, act_credits_2=j2)
            print("2nd sem haha "+ a2, b2, c2, d2 , e2, f2)
    
    return redirect('/grades')

# def save_grade_2(request):
#     if request.method == 'POST':
#         ids= request.POST.getlist('ids')
#         act1 = request.POST.getlist('act1')
#         act2 = request.POST.getlist('act2')
#         act3 = request.POST.getlist('act3')
#         act4 = request.POST.getlist('act4')
#         act5 = request.POST.getlist('act5')
#         act6 = request.POST.getlist('act6')
#         for a, b, c, d , e, f, i in zip(act1, act2, act3, act4, act5, act6, ids):
#             extenduser.objects.filter(id=i).update(act1=a, act2=b, act3=c,act4=d, act5=e, act6=f)
#     return redirect('/grades')



def edit_activities(request, id):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        title = request.POST.get('title')
        act_numbers = request.POST.get('act_numbers')
        print(ids, title, act_numbers)
        
        activity.objects.filter(id=ids).update(act_title=title, act_numbers=act_numbers)

        return redirect('/grades')
    return redirect('/grades')

def delete_activities(request, id):
    activity.objects.filter(id=id).delete()
    messages.success(request, 'Deleted')
    return redirect('/grades')

def delete_td(request, id):
    training_day.objects.filter(id=id).delete()
    messages.success(request, 'Deleted')
    return redirect('/attendance_tab')
def delete_midterm(request, id):
    midterm.objects.filter(id=id).delete()
    messages.success(request, 'Deleted')
    return redirect('/midterms')

def delete_finals(request, id):
    finals.objects.filter(id=id).delete()
    messages.success(request, 'Deleted')
    return redirect('/finals_')

def attendance_tab(request):
    acts2 = training_day.objects.all()
    section2 = sections.objects.filter(fiel='ROTC')
    context = {
        'section2':section2,
        'acts2': acts2,
    }
    return render(request, 'activities/attendance_tab.html', context)

@login_required(login_url='/staff_signin')
def midterms(request):
    if request.user.is_staff:
    
        acts3 = midterm.objects.all()
        section2 = sections.objects.filter(fiel='ROTC')
        context = {
            'section2':section2,
            'acts3': acts3,
        }
        return render(request, 'activities/midterm.html', context)
    return redirect('/staff_signin')

def add_midterm(request):
    semester = request.POST.get('sem')
    date = request.POST.get('date')
    items = request.POST.get('items')
    print(semester, date, items)
    datas = midterm(semester=semester, date=date, items=items)
    datas.save()
    return redirect('/midterms')


def modify_midterm(request):
    #  first = midterm.objects.aggregate(TOTAL = Sum('items'))['TOTAL']
    first = midterm.objects.filter(semester='1st sem')
    second = midterm.objects.filter(semester='2nd Sem')
    if request.method == 'POST':
        getSection = request.POST.get('getSection')
        content4 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        context = {
            'content4':content4,
            'getSection':getSection,
            'first':first,
            'second':second
        }
        return render(request, 'activities/modify_midterm.html', context)
    return render(request, 'activities/modify_midterm.html', context)

def save_midterm(request):
    if request.method == 'POST':
        ids= request.POST.getlist('ids')
        midterm1 = request.POST.getlist('midterm1')
        midterm2 = request.POST.getlist('midterm2')
        subtot = request.POST.getlist('subtot')
        credits2 = request.POST.getlist('credits2')
        
        for a, b, c in zip(ids, midterm1, subtot):
            extenduser.objects.filter(id=a).update(midterm1=b, midterm1_credits=c)
            
        for a, b, c in zip(ids, midterm2, credits2):
            extenduser.objects.filter(id=a).update(midterm2=b, midterm2_credits=c)

    return redirect('/midterms')

@login_required(login_url='/staff_signin')
def finals_(request):
    if request.user.is_staff:
        acts3 = finals.objects.all()
        section2 = sections.objects.filter(fiel='ROTC')
        context = {
            'section2':section2,
            'acts3': acts3,
        }
        return render(request, 'activities/finals.html', context)
    return redirect('/staff_signin')

def modify_finals(request):
    #  first = midterm.objects.aggregate(TOTAL = Sum('items'))['TOTAL']
    first = finals.objects.filter(semester='1st sem')
    second = finals.objects.filter(semester='2nd Sem')
    if request.method == 'POST':
        getSection = request.POST.get('getSection')
        content4 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        context = {
            'content4':content4,
            'getSection':getSection,
            'first':first,
            'second':second
        }
        return render(request, 'activities/modify_finals.html', context)
    return render(request, 'activities/modify_finals.html', context)

def add_finals(request):
    semester = request.POST.get('sem')
    date = request.POST.get('date')
    items = request.POST.get('items')
    print(semester, date, items)
    datas = finals(semester=semester, date=date, items=items)
    datas.save()
    return redirect('/finals_')

def save_finals(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids')
        finals1 = request.POST.getlist('finals1')
        subtot1 = request.POST.getlist('subtot1')
        
        ids2 = request.POST.getlist('ids2')
        finals2 = request.POST.getlist('finals2')
        subtot2 = request.POST.getlist('subtot2')
        
        for a, b, c in zip(ids, finals1, subtot1):
            extenduser.objects.filter(id=a).update(finals1=b, finals_credits1=c)
        for d, e,f in zip(ids2, finals2, subtot2):
            extenduser.objects.filter(id=d).update(finals2=e, finals_credits2=f)
        return redirect('/finals_')
    
@login_required(login_url='/staff_signin')
def final_grade(request):
    if request.user.is_staff:
        acts3 = finals.objects.all()
        section2 = sections.objects.filter(fiel='ROTC')
        context = {
            'section2':section2,
            'acts3': acts3,
        }
        return render(request, 'activities/final_grade.html', context)
    return redirect('/staff_signin')

def access_final_grade(request):
    if request.method == 'POST':
        getSection = request.POST.get('getSection')
        content4 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        context = {
            'content4':content4,
            'getSection':getSection
          
        }
    return render(request, 'activities/access.html', context)

def save_finale_grades(request):
    if request.method == 'POST':
        ids_2 = request.POST.getlist('ids_2')
        second_grade = request.POST.getlist('final_grade2')
        equivalent2 = request.POST.getlist('equivalent2')
        ids = request.POST.getlist('ids')
        first_sem_grade = request.POST.getlist('final_grade')
        equivalent = request.POST.getlist('equivalent')
        
      
        
        for a, b, c in zip(ids, first_sem_grade, equivalent):
            extenduser.objects.filter(id=a).update(final_grade=b, first_equivalents=c)
            messages.success(request, 'Final Grade Updated successfully')
        for  d, e, f in zip(ids_2, second_grade, equivalent2):
            
            extenduser.objects.filter(id=d).update(final_grade_2=e, second_equivalents=f)
            messages.success(request, 'Final Grade Updated successfully')
        return redirect('/final_grade')

@login_required(login_url='/staff_signin')
def merits(request):
    if request.user.is_staff:
        
        acts3 = finals.objects.all()
        section2 = sections.objects.filter(fiel='ROTC')
        context = {
            'section2':section2,
            'acts3': acts3,
        }
        return render(request, 'activities/merits.html', context)
    return redirect('/staff_signin')
def access_merits(request):
    getSection = request.POST.get('getSection')
    content4 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
    context = {
        'content4':content4,
        'getSection':getSection
        
    }
    return render(request, 'activities/access_merits.html', context)

def save_merits(request):
    ids = request.POST.getlist('ids')
    ids2 = request.POST.getlist('ids2')
    equivalent_merits = request.POST.getlist('equivalent_merits')
    equivalent_merits2 = request.POST.getlist('equivalent_merits2')
    
    for a, b in zip(ids,equivalent_merits):
        extenduser.objects.filter(id=a).update(equivalent_merits=b)
        messages.success(request, 'Merits Updated successfully')
    for c, d in zip(ids2,equivalent_merits2):
        extenduser.objects.filter(id=c).update(equivalent_merits2=d)
        messages.success(request, 'Merits Updated successfully')
    return redirect('/merits')



def approve2(request, id):
    stat2 = request.POST.get('getID')
    platoons = request.POST.get('platoons')
    extenduser.objects.filter(idnumber=stat2).update(status='ENROLLED', first_sem='ENROLLED' )
    messages.success(request, 'Student ' + str (stat2) + ' has been Approved !')
    sub = request.POST.get('emailtext')
    msg = request.POST.get('message')
    emaila = request.POST.get('rname')
    send_mail(sub, msg,'tupc.nstp@gmail.com',[emaila])
    return redirect('/admin_pending')


def decline2(request, id):
       
    stat2 = request.POST.get('getID2')
   
    print(stat2)
    extenduser.objects.filter(idnumber=stat2).update(status='REJECTED')
    messages.success(request, 'Student ' + str (stat2) + ' has been Rejected !')
    return redirect('/admin_pending')


def custom36(request):
    if request.method == 'POST':
        try:
            sub = request.POST.get('emailtext')
            msg = request.POST.get('message')
            emaila = request.POST.get('rname')
            send_mail(sub, msg,'tupc.nstp@gmail.com',[emaila])
            print(sub)
            return redirect(request.META['HTTP_REFERER'])
            # return redirect('/admin_view_profile')
 
        except ImportError:
            messages.success(request, 'Email Encountered some errors. Please Contact your Administrator')
    return redirect('/admin_view_profile')

def open_wala(request):
    return render(request, 'activities/wala.html')


# def open_csv(request,):

#     if request.method == 'POST':
        
#         file = request.FILES['filename'] 
#         decoded_file = file.read().decode('utf-8').splitlines()
#         reader = csv.DictReader(decoded_file)
#         print(reader)
#         for row in reader:
#             header = list(row.keys())
#             break
#         data = {}
#         for row in reader:
#             print("ahahaha"+str(row))
#             for i in header:
                
#                 values = []
#                 values.append(row.get(i))
#                 if i not in data:
#                     data[i] = values
#                 data[i].extend(values)
        
#         context = {
#             'header': header,
#             'data': data,
            
#         }
#         print("header ito"+str(header))
#         print("data itos" +str(data))
        
#         return render(request, 'activities/open_csv.html', context)
#     return render(request, 'activities/open_csv.html', context)
def before_csv(request):
    
    if request.method == 'POST':
        
        td_count = request.POST.get('td_count')
        date0 = request.POST.get('date')
        date1 = request.POST.get('date1')
        getSection = request.POST.get('getSection')
        student = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        context = {
         
            'getSection':getSection,
      
            'td_count':td_count,
            'student':student
          
        }
    return render(request, 'activities/before_csv.html', context)

def open_csv(request):
    semester = school_year.objects.all()
    if request.method == 'POST':
        td_count = request.POST.get('td_count')
        print(td_count)
        getSection = request.POST.get('getSection')
        csvfile = request.FILES['filename']
        df = pd.read_csv(csvfile)
        context = {    
            'columns': df.columns,
            'rows': df.to_dict('records'),
            'td_count':td_count,
            'getSection':getSection,
            'semester':semester
        }
        return render(request, 'activities/open_csv.html', context)
    
def read_attendance(request):

    if request.method == 'POST':
        ids = request.POST.getlist('ids')
        dates = request.POST.get('dates')
        demerits = request.POST.getlist('demerits')
        
        ids2 = request.POST.getlist('ids2')
        dates2 = request.POST.get('dates2')
        demerits2 = request.POST.getlist('demerits2')
        td_count = request.POST.get('td_count')
        
         # for first sem ##################################
        if td_count == str(1):
            for a,b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD1='1', TD1_dem=b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(2):
            for a,b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD2='1', TD2_dem=b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(3):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD3='1', TD3_dem=b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(4):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD4='1', TD4_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(5):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD5='1', TD5_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(6):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD6='1', TD6_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(7):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD7='1', TD7_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(8):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD8='1', TD8_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(9):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD9='1', TD9_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(10):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD10='1', TD10_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(11):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD11='1', TD11_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(12): 
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD12='1', TD12_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(13):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD13='1', TD13_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(14):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD14='1', TD14_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(15):
            for a, b in zip(ids, demerits):
                extenduser.objects.filter(idnumber=a).update(TD15='1', TD15_dem = b)
                messages.success(request, 'Attendance and Demerits updated')
                
                
                
                #for second semester attendance
        if td_count == str(1):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1', TD1_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(2):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD2_2='1', TD2_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(3):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD3_2='1', TD3_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(4):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD4_2='1', TD4_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(5):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD5_2='1', TD5_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(6):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD6_2='1', TD6_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(7):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD7_2='1', TD7_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(8):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD8_2='1', TD8_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(9):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD9_2='1', TD9_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(10):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD10_2='1', TD10_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(11):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD11_2='1', TD11_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(12):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD12_2='1', TD12_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(13):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD13_2='1', TD13_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(14):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD14_2='1', TD14_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
        if td_count == str(15):
            for c, d in zip(ids2, demerits2): 
                extenduser.objects.filter(idnumber=c).update(TD15_2='1', TD15_2_dem = d)
                messages.success(request, 'Attendance and Demerits updated')
    return redirect('/sample_attendance')



def update_section(request):
    checked = request.POST.getlist('cb_1')
    options = request.POST.getlist('options')
    for a in checked:
        extenduser.objects.filter(id=a).update(status=options[0], first_sem=options[0])
    return redirect ('/manage_section')


@login_required(login_url='/staff_signin')
def cwts_attendance(request):
    if request.user.is_staff:
        section = sections.objects.all()
        date = cwts_training.objects.all()

        context = {
            'date':date, 
            'section':section,
        }

        return render(request, 'activities/cwts_attendance.html', context)
    return redirect('/staff_signin')

def cwts_td(request):
    if request.method == 'POST':
        class_td = request.POST.get('class_td')
        td_count = request.POST.get('td_count')
        if cwts_training.objects.filter(class_td=class_td).exists():
            messages.error(request, 'Training Day already exists ' +str(class_td))
            return redirect('/cwts_attendance')
        elif cwts_training.objects.filter(td_count =td_count).exists():
            messages.error(request, 'Training Day count exists ' +str(td_count))
            return redirect('/cwts_attendance')
        else:
            alls = cwts_training(class_td=class_td, td_count=td_count)
            alls.save()
            return redirect('/cwts_attendance')
    return redirect('/cwts_attendance')

def open_cwts_date(request):
    section = sections.objects.filter(fiel = 'CWTS')
    if request.method == 'POST':
        td_count = request.POST.get('td_count')
        cwts_td = request.POST.get('cwts_td')
        context = {
            'cwts_td':cwts_td,
            'section':section,
            'td_count':td_count
        }
        return render(request, 'activities/cwts_date.html', context)
    return render(request, 'activities/cwts_date.html')


def display_csv(request):
    
    if request.method == 'POST':
        
        td_count = request.POST.get('td_count')
        # date0 = request.POST.get('date')
        # date1 = request.POST.get('date1')
        getSection = request.POST.get('getSection')
        student = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        context = {
         
            'getSection':getSection,
      
            'td_count':td_count,
            'student':student
          
        }
    return render(request, 'activities/display_csv.html', context)


def open_cwts_csv(request):
    semester = school_year.objects.all()
    if request.method == 'POST':
        td_count = request.POST.get('td_count')
        getSection = request.POST.get('getSection')
        csvfile = request.FILES['filename']
        df = pd.read_csv(csvfile)
        context = {    
            'columns': df.columns,
            'rows': df.to_dict('records'),
            'td_count':td_count,
            'getSection':getSection,
            'semester':semester
        }
        return render(request, 'activities/read_csv.html', context)
    
    
    
def save_cwts_attendance(request):
    
    if request.method == 'POST':
        ids = request.POST.getlist('ids')
  
        # demerits = request.POST.getlist('demerits')
        
        ids2 = request.POST.getlist('ids2')
        
        # demerits2 = request.POST.getlist('demerits2')
        td_count = request.POST.get('td_count')
        
        print("id ito" +str(td_count) )
        
         # for first sem ##################################
        if td_count == str(1):
            for a in ids:
                extenduser.objects.filter(idnumber=a).update(TD1='1')
                messages.success(request, 'Attendance   x')
                print(a)
        if td_count == str(2):
            for a in ids :
                extenduser.objects.filter(idnumber=a).update(TD2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(3):
            for a in ids :
                extenduser.objects.filter(idnumber=a).update(TD3='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(4):
            for a in ids :
                extenduser.objects.filter(idnumber=a).update(TD4='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(5):
            for a in ids:
                extenduser.objects.filter(idnumber=a).update(TD5='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(6):
            for a in ids :
                extenduser.objects.filter(idnumber=a).update(TD6='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(7):
            for a in ids :
                extenduser.objects.filter(idnumber=a).update(TD7='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(8):
            for a in ids:
                extenduser.objects.filter(idnumber=a).update(TD8='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(9):
            for a in ids :
                extenduser.objects.filter(idnumber=a).update(TD9='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(10):
            for a in ids :
                extenduser.objects.filter(idnumber=a).update(TD10='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(11):
            for a in ids :
                extenduser.objects.filter(idnumber=a).update(TD11='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(12): 
            for a in ids:
                extenduser.objects.filter(idnumber=a).update(TD12='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(13):
            for a in ids:
                extenduser.objects.filter(idnumber=a).update(TD13='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(14):
            for a in ids:
                extenduser.objects.filter(idnumber=a).update(TD14='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(15):
            for a in ids:
                extenduser.objects.filter(idnumber=a).update(TD15='1')
                messages.success(request, 'Attendance   updated')
                
                
                
                #for second semester attendance
        if td_count == str(1):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(2):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(3):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(4):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(5):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(6):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(7):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(8):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(9):
            for c in ids2 : 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(10):
            for c in ids2 : 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(11):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(12):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(13):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(14):
            for c in ids2 : 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
        if td_count == str(15):
            for c in ids2: 
                extenduser.objects.filter(idnumber=c).update(TD1_2='1')
                messages.success(request, 'Attendance   updated')
    return redirect('/cwts_attendance')
def del_cwts_tday(request, id):
    
    cwts_training.objects.filter(id=id).delete()
    return redirect('/cwts_attendance')



# CWTS GRADING SYSTEM

@login_required(login_url='/staff_signin')
def cwts_attendance_tab(request):
    if request.user.is_staff:
        acts2 = cwts_training.objects.all()
        section2 = sections.objects.filter(fiel='CWTS')
        context = {
            'section2':section2,
            'acts2': acts2,
        }
        return render(request, 'activities/cwts_attendance_tab.html', context)
    return redirect('/staff_signin')


def cwts_show_students(request):
    counted = cwts_training.objects.values_list('td_count', flat=True).count()
    getSection = request.POST.get('getSection')
    content3 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
    content33 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED').count()
    attendance_percentage = cwts_grading.objects.all()
    context = {
        'content3':content3,
        'getSection':getSection,
        'counted':counted,
        'content33':content33,
        'attendance_percentage':[attendance_percentage.last()]
    }
    return render(request, 'activities/cwts_show_students.html', context)


# not yet done
def update_cwts_att_credits(request):
    if request.method == 'POST':
        ids = request.POST.getlist('getId')
        credits = request.POST.getlist('credits')
        ids2 = request.POST.getlist('ids2')
        credits2 = request.POST.getlist('credits2')
        print("creds "+ str(credits2))
        print("ids"+ str(ids2))
        
        for i, j in zip(ids, credits):
            print("id" + str(i), "creds"+ str(j))
            extenduser.objects.filter(id=i).update(att_credits=j)
        # extenduser.objects.filter
        
        for k, l in zip(ids2, credits2):
            extenduser.objects.filter(id=k).update(att_credits_2=l)
    return redirect('/attendance_tab')

def cwts_course_evaluation(request):
    evaluation = cwts_grading.objects.all()
    context = {
            'evaluation':[evaluation.last()],
    }
    return render(request, 'activities/cwts_grading.html', context)


def save_evaluation(request):
    if request.method == 'POST':
        attendance = request.POST.get('attendance')
        quiz = request.POST.get('quiz')
        exercise = request.POST.get('exercise')
        participation = request.POST.get('participation')
        midterm = request.POST.get('midterm')
        final = request.POST.get('final')
        total = request.POST.get('total')
        data = cwts_grading(attendance=attendance,quiz=quiz,exercises=exercise, participation=participation, midterm_exam=midterm, final_exam=final, total=total)
        data.save()
        messages.success(request, 'Grading Evaluation Updated Successfully')
    return redirect('/cwts_course_evaluation')


def update_att_credits_cwts(request):
    if request.method == 'POST':
        pres1 = request.POST.getlist('pres1')
        abs1 = request.POST.getlist('abs1')
        percentages = request.POST.getlist('percentage')
      

        ids = request.POST.getlist('getId')
        credits = request.POST.getlist('credits')
        ids2 = request.POST.getlist('ids2')
        credits2 = request.POST.getlist('credits2')
        print("creds "+ str(credits2))
        print("ids"+ str(ids2))
        
        for i, j, k, l, m in zip(ids, credits, pres1, abs1, percentages):
            extenduser.objects.filter(id=i).update(att_credits=j, pres1=k, abs1=l, percentage1=m)
        # extenduser.objects.filter
 
        
        for k, l in zip(ids2, credits2):
            extenduser.objects.filter(id=k).update(att_credits_2=l)
    return redirect('/cwts_attendance_tab')


def quiz(request):
    acts = cwts_activity.objects.all()
    section = sections.objects.filter(fiel= 'CWTS')
    context = {
        'section':section, 
        'acts': acts
    }
    return render(request, 'activities/quiz.html', context)

def add_quiz(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        count = request.POST.get('count')
        numbers = request.POST.get('numbers')
        print(title, count, numbers)
        if cwts_activity.objects.filter(act_count=numbers).exists():
            messages.error(request, 'Activity number ' +str(numbers)+ ' already exists'  )
        else:
            data = cwts_activity(act_title=title,act_count=numbers,  act_numbers=count)
            data.save()
    return redirect('/quiz')


def cwts_edit_activities(request, id):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        title = request.POST.get('title')
        act_numbers = request.POST.get('act_numbers')
        print(ids, title, act_numbers)
        
        cwts_activity.objects.filter(id=ids).update(act_title=title, act_numbers=act_numbers)

        return redirect('/quiz')
    return redirect('/quiz')


def cwts_delete_activities(request, id):
    cwts_activity.objects.filter(id=id).delete()
    messages.success(request, 'Deleted')
    return redirect('/quiz')



def cwts_modify_grades(request):
    total = cwts_activity.objects.aggregate(TOTAL = Sum('act_numbers'))['TOTAL']
    items = cwts_activity.objects.all()
    quiz_percentage = cwts_grading.objects.all()
    if request.method == 'POST':
        getSection = request.POST.get('getSection')
        content3 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        context = {
            'content3':content3,
            'getSection':getSection,
            'total':total,
            'items':items,
            'quiz_percentage':[quiz_percentage.last()]
        }
        return render(request, 'activities/cwts_modify.html', context)
    return render(request, 'activities/cwts_modify.html', context)

def cwts_save_grade(request):
    if request.method == 'POST':
        ids= request.POST.getlist('ids')
        
        credits1 = request.POST.getlist('credits1')
        credits2 = request.POST.getlist('credits2')
        print(ids)
        act1 = request.POST.getlist('act1')
        act2 = request.POST.getlist('act2')
        act3 = request.POST.getlist('act3')
        act4 = request.POST.getlist('act4')
        act5 = request.POST.getlist('act5')
        act6 = request.POST.getlist('act6')
        
        ids_2= request.POST.getlist('ids_2')
        act1_2 = request.POST.getlist('act1_2')
        act2_2 = request.POST.getlist('act2_2')
        act3_2 = request.POST.getlist('act3_2')
        act4_2 = request.POST.getlist('act4_2')
        act5_2 = request.POST.getlist('act5_2')
        act6_2 = request.POST.getlist('act6_2')
        # for a2 in (act1_2):
        for a, b, c, d , e, f , i, j in zip(act1, act2, act3, act4, act5, act6,  ids, credits1 ):
            extenduser.objects.filter(id=i).update(act1=a, act2=b, act3=c,act4=d, act5=e, act6=f, act_credits=j )
            messages.success(request, 'Updated successfully')
            
        for a2, b2, c2, d2 , e2, f2, i2, j2 in zip( act1_2, act2_2, act3_2, act4_2, act5_2, act6_2,  ids_2, credits2):
            extenduser.objects.filter(id=i2).update(act1_2=a2, act2_2=b2, act3_2=c2, act4_2=d2, act5_2=e2, act6_2=f2, act_credits_2=j2)
            messages.success(request, 'Updated successfully')
    
    return redirect('/quiz')



def exercises(request):
    acts = cwts_exercises.objects.all()
    section = sections.objects.filter(fiel= 'CWTS')
    context = {
        'section':section, 
        'acts': acts
    }
    return render(request, 'activities/exercises.html', context)



def cwts_access_exercises(request):
    total = cwts_exercises.objects.aggregate(TOTAL = Sum('act_numbers'))['TOTAL']
    items = cwts_exercises.objects.all()
    exercise_percentage = cwts_grading.objects.all()
    if request.method == 'POST':
        getSection = request.POST.get('getSection')
        content3 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        context = {
            'content3':content3,
            'getSection':getSection,
            'total':total,
            'items':items,
            'exercise_percentage':[exercise_percentage.last()]
        }
        return render(request, 'activities/cwts_exercise.html', context)
    return render(request, 'activities/cwts_exercise.html', context)



def add_exercises(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        count = request.POST.get('count')
        numbers = request.POST.get('numbers')
        print(title, count, numbers)
        if cwts_exercises.objects.filter(act_count=numbers).exists():
            messages.error(request, 'Exercises number ' +str(numbers)+ ' already exists'  )
        else:
            data = cwts_exercises(act_title=title,act_count=numbers,  act_numbers=count)
            data.save()
    return redirect('/exercises')


def cwts_save_exercises(request):
    if request.method == 'POST':
        ids= request.POST.getlist('ids')
        
        credits1 = request.POST.getlist('credits1')
        credits2 = request.POST.getlist('credits2')
        act1 = request.POST.getlist('act1')
        act2 = request.POST.getlist('act2')
        act3 = request.POST.getlist('act3')
        act4 = request.POST.getlist('act4')
        act5 = request.POST.getlist('act5')
        act6 = request.POST.getlist('act6')
        
        ids_2= request.POST.getlist('ids_2')
        act1_2 = request.POST.getlist('act1_2')
        act2_2 = request.POST.getlist('act2_2')
        act3_2 = request.POST.getlist('act3_2')
        act4_2 = request.POST.getlist('act4_2')
        act5_2 = request.POST.getlist('act5_2')
        act6_2 = request.POST.getlist('act6_2')
        # for a2 in (act1_2):
        for a, b, c, d , e, f , i, j in zip(act1, act2, act3, act4, act5, act6,  ids, credits1 ):
            extenduser.objects.filter(id=i).update(exe1=a, exe2=b, exe3=c,exe4=d, exe5=e, exe6=f, exe_credits=j )
            messages.success(request, 'Updated successfully')
            
        for a2, b2, c2, d2 , e2, f2, i2, j2 in zip( act1_2, act2_2, act3_2, act4_2, act5_2, act6_2,  ids_2, credits2):
            extenduser.objects.filter(id=i2).update(exe1_2=a2, exe2_2=b2, exe3_2=c2, exe4_2=d2, exe5_2=e2, exe6_2=f2, exe_credits2=j2)
            messages.success(request, 'Updated successfully')
    
    return redirect('/exercises')



def cwts_midterms(request):
    acts3 = cwts_midterm.objects.all()
    section2 = sections.objects.filter(fiel='CWTS')
    context = {
        'section2':section2,
        'acts3': acts3,
    }
    return render(request, 'activities/cwts_midterm.html', context)


def cwts_add_midterm(request):
    semester = request.POST.get('sem')
    date = request.POST.get('date')
    items = request.POST.get('items')
    if cwts_midterm.objects.filter(semester=semester).exists():
        messages.success(request, 'Semester already exists')
        return redirect('/cwts_midterms')
    print(semester, date, items)
    datas = cwts_midterm(semester=semester, date=date, items=items)
    datas.save()
    return redirect('/cwts_midterms')


def delete_cwts_midterm(request, id):
    cwts_midterm.objects.filter(id=id).delete()
    messages.success(request, 'Deleted')
    return redirect('/cwts_midterms')



def modify_cwts_midterm(request):
    #  first = midterm.objects.aggregate(TOTAL = Sum('items'))['TOTAL']
    first = cwts_midterm.objects.filter(semester='1st sem')
    second = cwts_midterm.objects.filter(semester='2nd Sem')
    
    midterm_percentage = cwts_grading.objects.all()
    if request.method == 'POST':
        getSection = request.POST.get('getSection')
        content4 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        context = {
            'content4':content4,
            'getSection':getSection,
            'first':first,
            'second':second, 
            'midterm_percentage':[midterm_percentage.last()]
        }
        return render(request, 'activities/modify_cwts_midterm.html', context)
    return render(request, 'activities/modify_cwts_midterm.html', context)




def save_cwts_midterm(request):
    if request.method == 'POST':
        ids= request.POST.getlist('ids')
        midterm1 = request.POST.getlist('midterm1')
        midterm2 = request.POST.getlist('midterm2')
        subtot = request.POST.getlist('subtot')
        credits2 = request.POST.getlist('credits2')
        
        for a, b, c in zip(ids, midterm1, subtot):
            extenduser.objects.filter(id=a).update(midterm1=b, midterm1_credits=c)
            
        for a, b, c in zip(ids, midterm2, credits2):
            extenduser.objects.filter(id=a).update(midterm2=b, midterm2_credits=c)

    return redirect('/cwts_midterms')


def cwts_finals(request):
    acts3 = cwts_final.objects.all()
    section2 = sections.objects.filter(fiel= 'CWTS')
    context = {
        'section2':section2,
        'acts3': acts3,
    }
    return render(request, 'activities/cwts_finals.html', context)


def modify_cwts_finals(request):
    #  first = midterm.objects.aggregate(TOTAL = Sum('items'))['TOTAL']
    first = cwts_final.objects.filter(semester='1st sem')
    second = cwts_final.objects.filter(semester='2nd Sem')
    finals_percentage = cwts_grading.objects.all()
    if request.method == 'POST':
        getSection = request.POST.get('getSection')
        content4 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        context = {
            'content4':content4,
            'getSection':getSection,
            'first':first,
            'second':second, 
            'finals_percentage':[finals_percentage.last()]
        }
        return render(request, 'activities/modify_cwts_finals.html', context)
    return render(request, 'activities/modify_cwts_finals.html', context)


def add_cwts_finals(request):
    semester = request.POST.get('sem')
    date = request.POST.get('date')
    items = request.POST.get('items')
    if cwts_final.objects.filter(semester=semester).exists():
        messages.success(request, 'Semester already exists')
        return redirect('/cwts_finals')
    print(semester, date, items)
    datas = cwts_final(semester=semester, date=date, items=items)
    datas.save()
    return redirect('/cwts_finals')



def save_cwts_finals(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids')
        finals1 = request.POST.getlist('finals1')
        subtot1 = request.POST.getlist('subtot1')
        
        ids2 = request.POST.getlist('ids2')
        finals2 = request.POST.getlist('finals2')
        subtot2 = request.POST.getlist('subtot2')
        
        for a, b, c in zip(ids, finals1, subtot1):
            extenduser.objects.filter(id=a).update(finals1=b, finals_credits1=c)
        for d, e,f in zip(ids2, finals2, subtot2):
            extenduser.objects.filter(id=d).update(finals2=e, finals_credits2=f)
        return redirect('/cwts_finals')
    
def delete_cwts_finals(request, id):
    cwts_final.objects.filter(id=id).delete()
    messages.success(request, 'Deleted')
    return redirect('/cwts_finals')

def cwts_final_grade(request):
    acts3 = cwts_final.objects.all()
    section2 = sections.objects.filter(fiel= 'CWTS')
    context = {
        'section2':section2,
        'acts3': acts3,
    }
    return render(request, 'activities/cwts_final_grade.html', context)

def access_cwts_final_grade(request):
    if request.method == 'POST':
        getSection = request.POST.get('getSection')
        content4 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        context = {
            'content4':content4,
            'getSection':getSection
          
        }
    return render(request, 'activities/cwts_access.html', context)




def save_cwts_finale_grades(request):
    if request.method == 'POST':
        ids_2 = request.POST.getlist('ids_2')
        second_grade = request.POST.getlist('final_grade2')
        equivalent2 = request.POST.getlist('equivalent2')
        ids = request.POST.getlist('ids')
        first_sem_grade = request.POST.getlist('final_grade')
        equivalent = request.POST.getlist('equivalent')
        
      
        
        for a, b, c in zip(ids, first_sem_grade, equivalent):
            extenduser.objects.filter(id=a).update(final_grade=b, first_equivalents=c)
            messages.success(request, 'Final Grade Updated successfully')
        for  d, e, f in zip(ids_2, second_grade, equivalent2):
            
            extenduser.objects.filter(id=d).update(final_grade_2=e, second_equivalents=f)
            messages.success(request, 'Final Grade Updated successfully')
        return redirect('/cwts_final_grade')
    
# helsth

def health(request):
    name = extenduser.objects.filter(user = request.user)
    details = extenduser.objects.filter(user=request.user)
    context = {
        'name':name,
        'details':details
    }
    return render(request, 'activities/others.html', context)
    
# @login_required(login_url='/login_page')
def edit_health(request):
    
    if request.method == 'POST':
        ids = request.POST.get('ids')
        # proof = request.FILES['proof']
        proof = extenduser.objects.get(id=ids)
    

        proof.proof = request.FILES['proof']
        if proof.proof != '':
            image_path = proof.proof.path
            if os.path.exists(image_path):
                os.remove(image_path)
            proof.save()
            
            sickness = request.POST.get('sickness')
            extenduser.objects.filter(id=ids).update(sickness=sickness)
        return redirect('/profile_page')

    return redirect('/profile_page')

    # proof = extenduser.objects.get(id=id)

    # proof.proof = request.FILES['proof']
    # image_path = proof.proof.path
    # if os.path.exists(image_path):
    #     os.remove(image_path)
    # proof.save()
    
    # file upload
def each_student(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    pres2 = extenduser.objects.filter(id=id)
    abs2= extenduser.objects.filter(id = id)
    present2 = []
    absent2 = []
    section = sections.objects.all()
    term = school_year.objects.all()
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id).filter(status='ENROLLED')
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
        
    for s in pres2:
        present2.append(s.pres2)
       
    for k in abs2:
        absent2.append(k.abs2)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1,
        'pres2':pres2,
        'abs2':abs2,
        'present2': present2,
        'absent2': absent2,
        'term':[term.last()],
    }
    

    
        
    return render(request, 'activities/each_student.html', context)
    



def update_each_student(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        current_datetime = datetime.datetime.now() 
        print("sheesh" + str(ids))
        
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber= request.POST.get('idnumber')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        section = request.POST.get('section')
        cpnumber = request.POST.get('cpnumber')
        civil = request.POST.get('civil')
        nationality = request.POST.get('nationality')
        nfather = request.POST.get('nfather')
        foccupation = request.POST.get('foccupation')
        nmother = request.POST.get('nmother')
        moccupation = request.POST.get('moccupation')
        pcontact = request.POST.get('pcontact')
        nguardian = request.POST.get('nguardian')
        gcontact = request.POST.get('gcontact')
        sickness = request.POST.get('sickness')
        field = request.POST.get('field')
        platoons = request.POST.get('platoons')
        note = request.POST.get('note')
        status = request.POST.get('status')
        modified_by = request.POST.get('modified_by')
        

        if status == 'PENDING' or status == 'DROPPED' or status == 'GRADUATE' :
            
            extenduser.objects.filter(id=ids).update(firstname = firstname,
            middlename = middlename,
            lastname=lastname,
            email = email,
            idnumber = idnumber,
            address = address,
            gender = gender,
            age = age,
            birthday = birthday,
            section = section, 
            cpnumber = cpnumber,
            civil = civil,
            nationality = nationality,
            nfather = nfather,
            foccupation = foccupation,
            nmother = nmother,
            moccupation = moccupation,
            pcontact = pcontact,
            nguardian = nguardian,
            gcontact = gcontact,
            sickness = sickness,
            field = field,
            platoons = platoons,
            note = note,
            status = status,
            date_joined = current_datetime,
            modified_by = modified_by,
            date_modified = current_datetime,


         
            
            )
            
            return redirect('/manage_section')
            
        else:
            extenduser.objects.filter(id=ids).update(firstname = firstname,
                middlename = middlename,
                lastname=lastname,
                email = email,
                idnumber = idnumber,
                address = address,
                gender = gender,
                age = age,
                birthday = birthday,
                section = section, 
                cpnumber = cpnumber,
                civil = civil,
                nationality = nationality,
                nfather = nfather,
                foccupation = foccupation,
                nmother = nmother,
                moccupation = moccupation,
                pcontact = pcontact,
                nguardian = nguardian,
                gcontact = gcontact,
                sickness = sickness,
                field = field,
                platoons = platoons,
                note = note,
                status = status,
                date_joined = current_datetime,
                modified_by = modified_by,
                date_modified = current_datetime,
            )
        
        
    
    # return redirect('/manage_section')
        return redirect(request.META['HTTP_REFERER'])

def custom999(request):
    if request.method == 'POST':
        try:
            sub = request.POST.get('subject')
            msg = request.POST.get('message')
            emaila = request.POST.get('rname')
            send_mail(sub, msg,'tupc.nstp@gmail.com',[emaila])
            print(sub)
            return redirect(request.META['HTTP_REFERER'])
            # return redirect('/admin_view_profile')
 
        except ImportError:
            messages.success(request, 'Email Encountered some errors. Please Contact your Administrator')
    return redirect('/manage_section')


@login_required(login_url='/staff_signin')
def manage_cwts_section(request):
    if request.user.is_staff:
        current_datetime = datetime.datetime.now() 
        userContent = User.objects.all()
        sectionxx = extenduser.objects.all()
        counts = extenduser.objects.filter(status='ENROLLED').count()
        counts1 = extenduser.objects.filter(status='ENROLLED')
        section = sections.objects.filter(fiel='CWTS')
        section1 = sections.objects.all().count()
        secCount = request.POST.get('secCount')
        # counts3 = extenduser.objects.filter(status='ENROLLED').filter(platoons='ALPHA')
        context = {
            
        'counts':counts,
        'counts1':counts1,
        'section':section,
        'section1':section1,
        'sectionxx':sectionxx,
        'userContent':userContent,
        'current_datetime':current_datetime,
        # 'counts3':counts3
        }
    
        print(secCount)
        return render(request, 'activities/manage_cwts_section.html', context)
    return redirect('/staff_signin')


@login_required(login_url='/staff_signin')
def cwts_section_content(request):
    if request.user.is_staff:
    
        userContent = User.objects.all()
        schools = school_year.objects.all()
        rotc_section = sections.objects.filter(fiel='CWTS')
        if request.method == 'POST':
        
            getSection = request.POST.get('getSection')
            print(getSection)
            content3 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
            content33 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED').count()
        else:
        
            return render(request, 'activities/cwts_pl_content.html')
        context = {
            'content3':content3,
            'userContent':userContent,
            'content33':content33,
            'getSection':getSection,
            'schools':[schools.last()],
            'section':rotc_section
            
        }
        print(content33)
        print(getSection)
        return render(request, 'activities/cwts_pl_content.html', context)
    return redirect('/staff_signin')



def cwts_each_student(request, id):
       
   
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id = id)
    abs1 = extenduser.objects.filter(id = id)
    pres2 = extenduser.objects.filter(id=id)
    abs2= extenduser.objects.filter(id = id)
    present2 = []
    absent2 = []
    section = sections.objects.all()
    term = school_year.objects.all()
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id).filter(status='ENROLLED')
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
        
    for s in pres2:
        present2.append(s.pres2)
       
    for k in abs2:
        absent2.append(k.abs2)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'present2': present2,
        'absent2': absent2,
        'name': name,
        'pres1':pres1,
        'abs1':abs1,
        'term':[term.last()]
    }
        
    return render(request, 'activities/cwts_each.html', context)

def cwts_each_student_2(request, id):
       
   
    section = sections.objects.all()
    ids= request.POST.get('ids')
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id).filter(status='ENROLLED')
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section
    }
    

    
        
    return render(request, 'activities/cwts_each.html', context)



def add_cwts_students(request):
    if request.method == 'POST':
        platoon = request.POST.get('platoon')
        allstudent = extenduser.objects.filter(status='ENROLLED').filter(platoons='PROCESSING').filter(field='CWTS')
    else:
        return redirect('/manage_section')
    context = {
        'allstudent':allstudent,
        'platoon':platoon
    }
    return render(request, 'activities/cwts_students_list.html', context)

def assign_cwts_section(request):
    if request.method == 'POST':
        platoons=request.POST.get('platoons')
        lists = request.POST.getlist('students[]')
        
        if lists != '':
            
 
            for s in lists:
                extenduser.objects.filter(id=s).update(platoons=platoons)
                print("id ito" +str(s))
                

       
    
            return redirect('/manage_cwts_section')
        else:
            return redirect('/manage_cwts_section')
    else:
        return redirect('/manage_cwts_section')
    
    
    
    # fil upload
    
def file_upload_index(request):
    allfile = rfiles.objects.all()
    platoons = sections.objects.filter(fiel='ROTC')
    context = {
        'allfile':allfile,
        'platoons':platoons
    }
    return render(request, 'activities/file_upload_preface.html', context)

def upload_file(request):
    current_datetime = datetime.datetime.now() 
    if request.method == 'POST':
        platoons = request.POST.get('platoons')
        files = request.FILES['files']
        note = request.POST.get('note')
        date = request.POST.get('date')
        data = rfiles(files=files, note=note, date_posted=current_datetime, platoons=platoons)
        data.save()
    return redirect('/file_upload_index')
        
def delete_files(request, id):
    rfiles.objects.filter(id=id).delete()

    return redirect('/file_upload_index')



def cwts_file_upload(request):
    allfile = cfiles.objects.all()
    platoons = sections.objects.filter(fiel='CWTS')
    context = {
        'allfile':allfile,
        'platoons':platoons
    }
    return render(request, 'activities/cwts_file_upload.html', context)

def cwts_upload_file(request):
    current_datetime = datetime.datetime.now() 
    if request.method == 'POST':
        platoons = request.POST.get('platoons')
        files = request.FILES['files']
        note = request.POST.get('note')
        date = request.POST.get('date')
        data = cfiles(files=files, note=note, date_posted=current_datetime, platoons=platoons)
        data.save()
    return redirect('/cwts_file_upload')

        
def delete_cfiles(request, id):
    cfiles.objects.filter(id=id).delete()

    return redirect('/cwts_file_upload')
#######################################
def add_alumni_years(request):
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        combine = (start +"-"+ end)
        if alumni_school_year.objects.filter(years=combine).exists():
            messages.error(request, 'School year ' + str (combine) + ' Already Exist !')
            return redirect('/rotc_alumni')
        else:
            data1 = alumni_school_year(years=combine)
            data1.save()
    return redirect('/rotc_alumni')


def rotc_alumni(request):
    school_years = alumni_school_year.objects.all().order_by('years')
    context = {
        'school_years':school_years
    }
    return render(request, 'activities/rotc_alumni.html', context)
    



def alumni_years(request):
    if request.method == 'POST':
        years = request.POST.get('years')
        
        peoples = extenduser.objects.filter(s_year = years).filter(status='GRADUATE').filter(field='ROTC')
        context = {
            'years': years,
            'peoples':peoples
        }
        return render(request, 'activities/alumni_content.html', context)
    return render(request, 'activities/alumni_content.html')



def each_alumni(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    section = sections.objects.all()
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id).filter(status='GRADUATE')
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1
    }
    

    
        
    return render(request, 'activities/each_alumni.html', context)

def update_each_graduates(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        
        print("sheesh" + str(ids))
        
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber= request.POST.get('idnumber')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        section = request.POST.get('section')
        cpnumber = request.POST.get('cpnumber')
        civil = request.POST.get('civil')
        nationality = request.POST.get('nationality')
        nfather = request.POST.get('nfather')
        foccupation = request.POST.get('foccupation')
        nmother = request.POST.get('nmother')
        moccupation = request.POST.get('moccupation')
        pcontact = request.POST.get('pcontact')
        nguardian = request.POST.get('nguardian')
        gcontact = request.POST.get('gcontact')
        sickness = request.POST.get('sickness')
        field = request.POST.get('field')
        platoons = request.POST.get('platoons')
        note = request.POST.get('note')
        status = request.POST.get('status')
        if status != 'GRADUATE' :
            
            extenduser.objects.filter(id=ids).update(firstname = firstname,
            middlename = middlename,
            lastname=lastname,
            email = email,
            idnumber = idnumber,
            address = address,
            gender = gender,
            age = age,
            birthday = birthday,
            section = section, 
            cpnumber = cpnumber,
            civil = civil,
            nationality = nationality,
            nfather = nfather,
            foccupation = foccupation,
            nmother = nmother,
            moccupation = moccupation,
            pcontact = pcontact,
            nguardian = nguardian,
            gcontact = gcontact,
            sickness = sickness,
            field = field,
            platoons = platoons,
            note = note,
            status = status
            
            )
            
            return redirect('/rotc_alumni')
            
        else:
            extenduser.objects.filter(id=ids).update(firstname = firstname,
                middlename = middlename,
                lastname=lastname,
                email = email,
                idnumber = idnumber,
                address = address,
                gender = gender,
                age = age,
                birthday = birthday,
                section = section, 
                cpnumber = cpnumber,
                civil = civil,
                nationality = nationality,
                nfather = nfather,
                foccupation = foccupation,
                nmother = nmother,
                moccupation = moccupation,
                pcontact = pcontact,
                nguardian = nguardian,
                gcontact = gcontact,
                sickness = sickness,
                field = field,
                platoons = platoons,
                note = note,
                status = status
            )
        
        
    
    # return redirect('/manage_section')
        return redirect(request.META['HTTP_REFERER'])
    
    
def cwts_alumni(request):
    school_years = alumni_school_year.objects.all()
    context = {
        'school_years':school_years
    }
    return render(request, 'activities/cwts_alumni.html', context)
    


def cwts_alumni_years(request):
    if request.method == 'POST':
        years = request.POST.get('years')
        
        peoples = extenduser.objects.filter(s_year = years).filter(status='GRADUATE').filter(field='CWTS')
        context = {
            'years': years,
            'peoples':peoples
        }
        return render(request, 'activities/cwts_alumni_content.html', context)
    return render(request, 'activities/cwts_alumni_content.html')

def cwts_each_alumni(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    section = sections.objects.all()
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id).filter(status='GRADUATE')
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1
    }
    

    
        
    return render(request, 'activities/cwts_each_alumni.html', context)




def update_each_cwts_graduates(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        
        print("sheesh" + str(ids))
        
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber= request.POST.get('idnumber')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        section = request.POST.get('section')
        cpnumber = request.POST.get('cpnumber')
        civil = request.POST.get('civil')
        nationality = request.POST.get('nationality')
        nfather = request.POST.get('nfather')
        foccupation = request.POST.get('foccupation')
        nmother = request.POST.get('nmother')
        moccupation = request.POST.get('moccupation')
        pcontact = request.POST.get('pcontact')
        nguardian = request.POST.get('nguardian')
        gcontact = request.POST.get('gcontact')
        sickness = request.POST.get('sickness')
        field = request.POST.get('field')
        platoons = request.POST.get('platoons')
        note = request.POST.get('note')
        status = request.POST.get('status')
        if status != 'GRADUATE' :
            
            extenduser.objects.filter(id=ids).update(firstname = firstname,
            middlename = middlename,
            lastname=lastname,
            email = email,
            idnumber = idnumber,
            address = address,
            gender = gender,
            age = age,
            birthday = birthday,
            section = section, 
            cpnumber = cpnumber,
            civil = civil,
            nationality = nationality,
            nfather = nfather,
            foccupation = foccupation,
            nmother = nmother,
            moccupation = moccupation,
            pcontact = pcontact,
            nguardian = nguardian,
            gcontact = gcontact,
            sickness = sickness,
            field = field,
            platoons = platoons,
            note = note,
            status = status
            
            )
            
            return redirect('/rotc_alumni')
            
        else:
            extenduser.objects.filter(id=ids).update(firstname = firstname,
                middlename = middlename,
                lastname=lastname,
                email = email,
                idnumber = idnumber,
                address = address,
                gender = gender,
                age = age,
                birthday = birthday,
                section = section, 
                cpnumber = cpnumber,
                civil = civil,
                nationality = nationality,
                nfather = nfather,
                foccupation = foccupation,
                nmother = nmother,
                moccupation = moccupation,
                pcontact = pcontact,
                nguardian = nguardian,
                gcontact = gcontact,
                sickness = sickness,
                field = field,
                platoons = platoons,
                note = note,
                status = status
            )
        
        
    
    # return redirect('/manage_section')
        return redirect(request.META['HTTP_REFERER'])
    
    
def alumni_year(request, id):
    
    alumni_school_year.objects.filter(id=id).delete()
    messages.info(request, 'Deleted')
    return redirect('/rotc_alumni')

def cwts_alumni_year(request, id):
    
    alumni_school_year.objects.filter(id=id).delete()
    messages.info(request, 'Deleted')
    return redirect('/rotc_alumni')



def send_feedback(request):
    date_time = datetime.datetime.now() 
    if request.method == 'POST':
       name = request.POST.get('name')
       email = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')
       data = feedback(sender=name, email=email, date_sent=date_time, subject=subject, message=message)
       data.save()
    return redirect('/contact_us')


def send_response(request, id):
    feed = feedback.objects.filter(status = 'PENDING').order_by('date_sent')
    audience = sections.objects.all()
    ann = Announcement.objects.all()
    sy = school_year.objects.all()
    nav_pending_count = extenduser.objects.filter(status='PENDING').count()
    nav_rejected_count = extenduser.objects.filter(status='REJECTED').count()
    active = extenduser.objects.filter(status='ENROLLED').count()
    pending = extenduser.objects.filter(status='PENDING').count()

   

    id = id
    
    details = feedback.objects.filter(id=id)
    
    context = {
        'id': id,
        'details': details,
        'active':active,   
        'pending':pending,
        'sy':[sy.last()],
        'audience':audience,
        'ann':ann,
        # 'staff':staff,
        'nav_pending_count':nav_pending_count,
        'nav_rejected_count':nav_rejected_count ,
        'feed':feed
    }
    return render(request, 'activities/popup.html', context)


    
def student_update(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        all_id = extenduser.objects.get(id=ids)
        
        
        print("sheesh" + str(all_id.proof))
        
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber= request.POST.get('idnumber')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        section = request.POST.get('section')
        cpnumber = request.POST.get('cpnumber')
        civil = request.POST.get('civil')
        nationality = request.POST.get('nationality')
        nfather = request.POST.get('nfather')
        foccupation = request.POST.get('foccupation')
        nmother = request.POST.get('nmother')
        moccupation = request.POST.get('moccupation')
        pcontact = request.POST.get('pcontact')
        nguardian = request.POST.get('nguardian')
        gcontact = request.POST.get('gcontact')
        field = request.POST.get('field')
        sickness = request.POST.get('sickness')
        
      
        status = request.POST.get('status')
        if len(request.FILES) != 0:
            if all_id.proof:
                os.remove(all_id.proof.path)
            else:
                print("ERROR")
                all_id.proof = request.FILES['proof']
                all_id.save()
        if status == 'PENDING' or status == 'DROPPED' or status == 'GRADUATE' :
            
            extenduser.objects.filter(user=request.user).update(firstname = firstname,
            middlename = middlename,
            lastname=lastname,
            email = email,
            idnumber = idnumber,
            address = address,
            gender = gender,
            age = age,
            birthday = birthday,
            section = section, 
            cpnumber = cpnumber,
            civil = civil,
            nationality = nationality,
            nfather = nfather,
            foccupation = foccupation,
            nmother = nmother,
            moccupation = moccupation,
            pcontact = pcontact,
            nguardian = nguardian,
            gcontact = gcontact,
       
            field = field,
  
            status = status,
            sickness=sickness,
        
            
            )

            
            return redirect('/profile_page')
            
        else:
            extenduser.objects.filter(user=request.user).update(firstname = firstname,
                middlename = middlename,
                lastname=lastname,
                email = email,
                idnumber = idnumber,
                address = address,
                gender = gender,
                age = age,
                birthday = birthday,
                section = section, 
                cpnumber = cpnumber,
                civil = civil,
                nationality = nationality,
                nfather = nfather,
                foccupation = foccupation,
                nmother = nmother,
                moccupation = moccupation,
                pcontact = pcontact,
                nguardian = nguardian,
                gcontact = gcontact,
                field = field,
                sickness=sickness,
        
          
            
                
            )

    
    return redirect('/profile_page')
        # return redirect(request.META['HTTP_REFERER'])
@login_required(login_url='/login_page')
def all_files(request):
    name = extenduser.objects.filter(user = request.user)
    userplatoon = extenduser.objects.filter(user=request.user)
    files = rfiles.objects.all()
    context = {
        'userplatoon':userplatoon,
        'files': files,
        'name':name
    }
    return render(request, 'activities/display_file.html', context)



def update_each_pending(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        
        print("sheesh" + str(ids))
        
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber= request.POST.get('idnumber')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        section = request.POST.get('section')
        cpnumber = request.POST.get('cpnumber')
        civil = request.POST.get('civil')
        nationality = request.POST.get('nationality')
        nfather = request.POST.get('nfather')
        foccupation = request.POST.get('foccupation')
        nmother = request.POST.get('nmother')
        moccupation = request.POST.get('moccupation')
        pcontact = request.POST.get('pcontact')
        nguardian = request.POST.get('nguardian')
        gcontact = request.POST.get('gcontact')
        sickness = request.POST.get('sickness')
        field = request.POST.get('field')
        platoons = request.POST.get('platoons')
        note = request.POST.get('note')
        status = request.POST.get('status')
        approved_by = request.POST.get('approved_by')
        date_declined = datetime.datetime.now()
        platoon_count = extenduser.objects.filter(platoons=platoons).count()
        
        term = request.POST.get('term')
        first_sem = request.POST.get('first_sem')
        second_sem = request.POST.get('second_sem')
        print("hahahah" +str(platoon_count))
        if platoon_count < 29 :
            if term == 'First Term':
   
                if status == 'PENDING':
                    
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                    middlename = middlename,
                    lastname=lastname,
                    email = email,
                    idnumber = idnumber,
                    address = address,
                    gender = gender,
                    age = age,
                    birthday = birthday,
                    section = section, 
                    cpnumber = cpnumber,
                    civil = civil,
                    nationality = nationality,
                    nfather = nfather,
                    foccupation = foccupation,
                    nmother = nmother,
                    moccupation = moccupation,
                    pcontact = pcontact,
                    nguardian = nguardian,
                    gcontact = gcontact,
                    sickness = sickness,
                    field = field,
                    platoons = platoons,
                    note = note,
                    status = status,
            
                    approved_by = approved_by,
                    date_declined = date_declined,
                    
                    
                    )
                    
                    return redirect('/admin_pending')
                    
                elif status == 'ENROLLED':
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                        first_sem = first_sem,
                        second_sem = second_sem,
                        approved_by = approved_by,
                        date_declined = date_declined,
                    )
                    return redirect('/admin_pending')
                    # return redirect(request.META['HTTP_REFERER'])
                elif status == 'REJECTED':
                
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                        first_sem = status,
                        second_sem= second_sem,
                        approved_by = approved_by,
                        date_declined = date_declined,
                        
                    
                    )
                    
                return redirect('/admin_pending')
            
            elif term == 'Second Term':
                   
                if status == 'PENDING':
                    
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                    middlename = middlename,
                    lastname=lastname,
                    email = email,
                    idnumber = idnumber,
                    address = address,
                    gender = gender,
                    age = age,
                    birthday = birthday,
                    section = section, 
                    cpnumber = cpnumber,
                    civil = civil,
                    nationality = nationality,
                    nfather = nfather,
                    foccupation = foccupation,
                    nmother = nmother,
                    moccupation = moccupation,
                    pcontact = pcontact,
                    nguardian = nguardian,
                    gcontact = gcontact,
                    sickness = sickness,
                    field = field,
                    platoons = platoons,
                    note = note,
                    status = status,
            
                    approved_by = approved_by,
                    date_declined = date_declined,
                    
                    
                    )
                    
                    return redirect('/admin_pending')
                    
                elif status == 'ENROLLED':
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                        first_sem = first_sem,
                        second_sem = second_sem,
                        approved_by = approved_by,
                        date_declined = date_declined,
                    )
                    return redirect('/admin_pending')
                    # return redirect(request.META['HTTP_REFERER'])
                elif status == 'REJECTED':
                
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                        first_sem = first_sem,
                        second_sem= status,
                        approved_by = approved_by,
                        date_declined = date_declined,
                        
                    
                    )
                    
                return redirect('/admin_pending')
                
        else:
            messages.info(request,  str(platoons) + ' platoon has reached the maximum number of students')
            
        
        # return redirect('/manage_section')
            return redirect(request.META['HTTP_REFERER'])

def update_cwts_each_pending(request):
        if request.method == 'POST':
            ids = request.POST.get('ids')
        
        print("sheesh" + str(ids))
        
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber= request.POST.get('idnumber')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        section = request.POST.get('section')
        cpnumber = request.POST.get('cpnumber')
        civil = request.POST.get('civil')
        nationality = request.POST.get('nationality')
        nfather = request.POST.get('nfather')
        foccupation = request.POST.get('foccupation')
        nmother = request.POST.get('nmother')
        moccupation = request.POST.get('moccupation')
        pcontact = request.POST.get('pcontact')
        nguardian = request.POST.get('nguardian')
        gcontact = request.POST.get('gcontact')
        sickness = request.POST.get('sickness')
        field = request.POST.get('field')
        platoons = request.POST.get('platoons')
        note = request.POST.get('note')
        status = request.POST.get('status')
        approved_by = request.POST.get('approved_by')
        date_declined = datetime.datetime.now()
        platoon_count = extenduser.objects.filter(platoons=platoons).count()
        
        term = request.POST.get('term')
        first_sem = request.POST.get('first_sem')
        second_sem = request.POST.get('second_sem')
        print("hahahah" +str(platoon_count))
        if platoon_count < 29 :
            if term == 'First Term':
   
                if status == 'PENDING':
                    
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                    middlename = middlename,
                    lastname=lastname,
                    email = email,
                    idnumber = idnumber,
                    address = address,
                    gender = gender,
                    age = age,
                    birthday = birthday,
                    section = section, 
                    cpnumber = cpnumber,
                    civil = civil,
                    nationality = nationality,
                    nfather = nfather,
                    foccupation = foccupation,
                    nmother = nmother,
                    moccupation = moccupation,
                    pcontact = pcontact,
                    nguardian = nguardian,
                    gcontact = gcontact,
                    sickness = sickness,
                    field = field,
                    platoons = platoons,
                    note = note,
                    status = status,
            
                    approved_by = approved_by,
                    date_declined = date_declined,
                    
                    
                    )
                    
                    return redirect('/admin_pending')
                    
                elif status == 'ENROLLED':
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                        first_sem = first_sem,
                        second_sem = second_sem,
                        approved_by = approved_by,
                        date_declined = date_declined,
                    )
                    return redirect('/admin_pending')
                    # return redirect(request.META['HTTP_REFERER'])
                elif status == 'REJECTED':
                
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                        first_sem = status,
                        second_sem= second_sem,
                        approved_by = approved_by,
                        date_declined = date_declined,
                        
                    
                    )
                    
                return redirect('/admin_pending')
            
            elif term == 'Second Term':
                   
                if status == 'PENDING':
                    
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                    middlename = middlename,
                    lastname=lastname,
                    email = email,
                    idnumber = idnumber,
                    address = address,
                    gender = gender,
                    age = age,
                    birthday = birthday,
                    section = section, 
                    cpnumber = cpnumber,
                    civil = civil,
                    nationality = nationality,
                    nfather = nfather,
                    foccupation = foccupation,
                    nmother = nmother,
                    moccupation = moccupation,
                    pcontact = pcontact,
                    nguardian = nguardian,
                    gcontact = gcontact,
                    sickness = sickness,
                    field = field,
                    platoons = platoons,
                    note = note,
                    status = status,
            
                    approved_by = approved_by,
                    date_declined = date_declined,
                    
                    
                    )
                    
                    return redirect('/admin_pending')
                    
                elif status == 'ENROLLED':
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                        first_sem = first_sem,
                        second_sem = second_sem,
                        approved_by = approved_by,
                        date_declined = date_declined,
                    )
                    return redirect('/admin_pending')
                    # return redirect(request.META['HTTP_REFERER'])
                elif status == 'REJECTED':
                
                    extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                        first_sem = first_sem,
                        second_sem= status,
                        approved_by = approved_by,
                        date_declined = date_declined,
                        
                    
                    )
                    
                return redirect('/admin_pending')
                
        else:
            messages.info(request,  str(platoons) + ' platoon has reached the maximum number of students')
            
        
        # return redirect('/manage_section')
            return redirect(request.META['HTTP_REFERER'])
    
    
def search(request):
    return render(request, 'activities/searching.html')

# def search_on(request):
#     results = []
#     if request.method == "POST":
#         query = request.POST.get('search')
#         if query == '':
#             query = 'None'
#         results = extenduser.objects.filter(Q(firstname__icontains=query) | Q(lastname__icontains=query) | Q(idnumber__icontains=query) )
#     return render(request, 'search.html', {'query': query, 'results': results})


def search_on(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        details = extenduser.objects.filter(firstname = firstname).filter(lastname = lastname).filter(status='GRADUATE')
        count = extenduser.objects.filter(firstname = firstname).filter(lastname = lastname).filter(status='GRADUATE').count()
        print(details)
        context  = {
            'details':details,
            'count':count
        }
        
    return render(request, 'activities/results.html', context)

def contact_us(request):
    # sss
    return render(request, 'activities/contact_us.html')



@login_required(login_url='/staff_signin')
def school_years(request):
    if request.user.is_superuser:
        
        s_years = school_year.objects.all()
        alls = school_year.objects.all().order_by('years').reverse()
        ss_years = extenduser.objects.all()
        ewan = school_year.objects.all()

    
        context = {
            'ewan':ewan,
            's_years':[s_years.last()],
            'ss_years':ss_years,
            'alls':alls
            # 'graduates':graduates
            
        }

        return render(request, 'activities/sy.html', context)
    return redirect('/staff_signin')



def create_sy(request):
    
        if request.method == 'POST':
            start  = request.POST.get('start')
            end =  request.POST.get('end')
            
            combine = (start +"-"+ end)
            print(combine)
            
            
            
            
            
            if request.user.is_superuser:
                if school_year.objects.filter(years=combine).exists():
                    messages.info(request, 'School year ' + str (combine) + ' ALready exist !')
                    return redirect('/school_years')
                elif alumni_school_year.objects.filter(years=combine).exists():
                    data = school_year(years=combine)

                    data.save()
            
                    return redirect('/school_years')


                else:
                    data = school_year(years=combine)
                    data2 = alumni_school_year(years=combine)
                    data.save()
                    data2.save()
                
                    messages.success(request, 'School year ' + str (combine) + ' Successfully Created !')
                    return redirect('/school_years')
            else:
                messages.success(request, 'You Are not authorize to Modify School Year \nPlease Contact your Administrator')
        return redirect('/school_years')
   


def update_sel(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        status = request.POST.get('status')
        sem = request.POST.get('sem')
        
        school_year.objects.filter(years=year).update(status=status, sem=sem)
    return redirect('/school_years')

def delete_sy(request, years):
    school_year.objects.filter(years=years).delete()
    alumni_school_year.objects.filter(years=years).delete()
    print(id)
    return redirect('/school_years')

# done
@login_required(login_url='/staff_signin')
def admin_pending(request):
    if request.user.is_staff:
    
        s_years = school_year.objects.all()
        platoons = sections.objects.all()
        pending = extenduser.objects.filter(status='PENDING').count()
        pendings = extenduser.objects.filter(status='PENDING', field='ROTC')
        context = {
            'pendings':pendings,
            'pending':pending,
            'platoons':platoons,
            's_years':[s_years.last()],
        }
        return render(request, 'activities/admin_pending.html', context)
    return redirect('/staff_signin')



@login_required(login_url='/staff_signin')
def cwts_admin_pending(request):
    if request.user.is_staff:
        s_years = school_year.objects.all()
        platoons = sections.objects.all()
        pending = extenduser.objects.filter(status='PENDING').count()
        pendings = extenduser.objects.filter(status='PENDING' , field='CWTS')
        context = {
            'pendings':pendings,
            'pending':pending,
            'platoons':platoons,
            's_years':[s_years.last()],
        }
        return render(request, 'activities/cwts_admin_pending.html', context)
    return redirect('/staff_signin')
def response(request):
    if request.method == 'POST':
        try:
            sub = request.POST.get('emailtext')
            msg = request.POST.get('message')
            email = request.POST.get('email')
            send_mail(sub, msg,'tupc.nstp@gmail.com',[email])
            return redirect('/admin_dashboard')
        except ImportError:
            messages.success(request, 'Email Encountered some errors. Please Contact your Administrator')
    return redirect('/admin_dashboard')


def update_mess(request):
    if request.method == 'POST':
        action_date = datetime.datetime.now() 
        actionby = request.POST.get('action')
        ids = request.POST.get('ids')
        status = request.POST.get('status')

        feedback.objects.filter(id=ids).update(status = status, action_by = actionby, action_date=action_date)
        

    return redirect('/admin_dashboard')


def mess_history(request):
    details = feedback.objects.filter(status = 'DONE')
    context = {
        'details':details,
    }
    return render(request, 'activities/history.html', context)

def del_ans(request, id):
    feedback.objects.filter(id=id).delete()
 

    return redirect('/mess_history')





def rejected_rotc_profile(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    section = sections.objects.all()
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id)
    sy = school_year.objects.all()
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1,
        'sy':[sy.last()]
    }
    

    
    return render(request, 'activities/rejected_rotc_profile.html', context)


def rejected_custom(request):
    if request.method == 'POST':
        try:
            sub = request.POST.get('subject')
            msg = request.POST.get('message')
            emaila = request.POST.get('rname')
            send_mail(sub, msg,'tupc.nstp@gmail.com',[emaila])
            print(sub)
            return redirect(request.META['HTTP_REFERER'])
            # return redirect('/admin_view_profile')
 
        except ImportError:
            messages.success(request, 'Email Encountered some errors. Please Contact your Administrator')
    return redirect('/admin_rejected')


def update_each_rejected(request):
    if request.method == 'POST':
            ids = request.POST.get('ids')
            
            print("sheesh" + str(ids))
            
            firstname = request.POST.get('firstname')
            middlename = request.POST.get('middlename')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            idnumber= request.POST.get('idnumber')
            address = request.POST.get('address')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            birthday = request.POST.get('birthday')
            section = request.POST.get('section')
            cpnumber = request.POST.get('cpnumber')
            civil = request.POST.get('civil')
            nationality = request.POST.get('nationality')
            nfather = request.POST.get('nfather')
            foccupation = request.POST.get('foccupation')
            nmother = request.POST.get('nmother')
            moccupation = request.POST.get('moccupation')
            pcontact = request.POST.get('pcontact')
            nguardian = request.POST.get('nguardian')
            gcontact = request.POST.get('gcontact')
            sickness = request.POST.get('sickness')
            field = request.POST.get('field')
            platoons = request.POST.get('platoons')
            note = request.POST.get('note')
            status = request.POST.get('status')
            approved_by = request.POST.get('approved_by')
            date_declined = datetime.datetime.now()
            platoon_count = extenduser.objects.filter(platoons=platoons).count()
            
            term = request.POST.get('term')
            first_sem = request.POST.get('first_sem')
            second_sem = request.POST.get('second_sem')
            print("hahahah" +str(platoon_count))
            if platoon_count < 29 :
                if term == 'First Term':
    
                    if status == 'PENDING':
                        
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                
                        approved_by = approved_by,
                        date_declined = date_declined,
                        
                        
                        )
                        
                        return redirect('/admin_pending')
                        
                    elif status == 'ENROLLED':
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                            middlename = middlename,
                            lastname=lastname,
                            email = email,
                            idnumber = idnumber,
                            address = address,
                            gender = gender,
                            age = age,
                            birthday = birthday,
                            section = section, 
                            cpnumber = cpnumber,
                            civil = civil,
                            nationality = nationality,
                            nfather = nfather,
                            foccupation = foccupation,
                            nmother = nmother,
                            moccupation = moccupation,
                            pcontact = pcontact,
                            nguardian = nguardian,
                            gcontact = gcontact,
                            sickness = sickness,
                            field = field,
                            platoons = platoons,
                            note = note,
                            status = status,
                            first_sem = first_sem,
                            second_sem = second_sem,
                            approved_by = approved_by,
                            date_declined = date_declined,
                        )
                        return redirect('/admin_pending')
                        # return redirect(request.META['HTTP_REFERER'])
                    elif status == 'REJECTED':
                    
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                            middlename = middlename,
                            lastname=lastname,
                            email = email,
                            idnumber = idnumber,
                            address = address,
                            gender = gender,
                            age = age,
                            birthday = birthday,
                            section = section, 
                            cpnumber = cpnumber,
                            civil = civil,
                            nationality = nationality,
                            nfather = nfather,
                            foccupation = foccupation,
                            nmother = nmother,
                            moccupation = moccupation,
                            pcontact = pcontact,
                            nguardian = nguardian,
                            gcontact = gcontact,
                            sickness = sickness,
                            field = field,
                            platoons = platoons,
                            note = note,
                            status = status,
                            first_sem = status,
                            second_sem= second_sem,
                            approved_by = approved_by,
                            date_declined = date_declined,
                            
                        
                        )
                        
                    return redirect('/admin_pending')
                
                elif term == 'Second Term':
                    
                    if status == 'PENDING':
                        
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                
                        approved_by = approved_by,
                        date_declined = date_declined,
                        
                        
                        )
                        
                        return redirect('/admin_pending')
                        
                    elif status == 'ENROLLED':
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                            middlename = middlename,
                            lastname=lastname,
                            email = email,
                            idnumber = idnumber,
                            address = address,
                            gender = gender,
                            age = age,
                            birthday = birthday,
                            section = section, 
                            cpnumber = cpnumber,
                            civil = civil,
                            nationality = nationality,
                            nfather = nfather,
                            foccupation = foccupation,
                            nmother = nmother,
                            moccupation = moccupation,
                            pcontact = pcontact,
                            nguardian = nguardian,
                            gcontact = gcontact,
                            sickness = sickness,
                            field = field,
                            platoons = platoons,
                            note = note,
                            status = status,
                            first_sem = first_sem,
                            second_sem = second_sem,
                            approved_by = approved_by,
                            date_declined = date_declined,
                        )
                        return redirect('/admin_pending')
                        # return redirect(request.META['HTTP_REFERER'])
                    elif status == 'REJECTED':
                    
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                            middlename = middlename,
                            lastname=lastname,
                            email = email,
                            idnumber = idnumber,
                            address = address,
                            gender = gender,
                            age = age,
                            birthday = birthday,
                            section = section, 
                            cpnumber = cpnumber,
                            civil = civil,
                            nationality = nationality,
                            nfather = nfather,
                            foccupation = foccupation,
                            nmother = nmother,
                            moccupation = moccupation,
                            pcontact = pcontact,
                            nguardian = nguardian,
                            gcontact = gcontact,
                            sickness = sickness,
                            field = field,
                            platoons = platoons,
                            note = note,
                            status = status,
                            first_sem = first_sem,
                            second_sem= status,
                            approved_by = approved_by,
                            date_declined = date_declined,
                            
                        
                        )
                        
                    return redirect('/admin_pending')
                    
            else:
                messages.info(request,  str(platoons) + ' platoon has reached the maximum number of students')
                
            
            # return redirect('/manage_section')
                return redirect(request.META['HTTP_REFERER'])
    
    
def rejected_cwts_profile(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    section = sections.objects.all()
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id)
    sy = school_year.objects.all()
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1,
        'sy':[sy.last()]
    }
    

    
    return render(request, 'activities/rejected_cwts_profile.html', context)

def update_each_cwts_rejected(request):
    if request.method == 'POST':
            ids = request.POST.get('ids')
            
            print("sheesh" + str(ids))
            
            firstname = request.POST.get('firstname')
            middlename = request.POST.get('middlename')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            idnumber= request.POST.get('idnumber')
            address = request.POST.get('address')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            birthday = request.POST.get('birthday')
            section = request.POST.get('section')
            cpnumber = request.POST.get('cpnumber')
            civil = request.POST.get('civil')
            nationality = request.POST.get('nationality')
            nfather = request.POST.get('nfather')
            foccupation = request.POST.get('foccupation')
            nmother = request.POST.get('nmother')
            moccupation = request.POST.get('moccupation')
            pcontact = request.POST.get('pcontact')
            nguardian = request.POST.get('nguardian')
            gcontact = request.POST.get('gcontact')
            sickness = request.POST.get('sickness')
            field = request.POST.get('field')
            platoons = request.POST.get('platoons')
            note = request.POST.get('note')
            status = request.POST.get('status')
            approved_by = request.POST.get('approved_by')
            date_declined = datetime.datetime.now()
            platoon_count = extenduser.objects.filter(platoons=platoons).count()
            
            term = request.POST.get('term')
            first_sem = request.POST.get('first_sem')
            second_sem = request.POST.get('second_sem')
            print("hahahah" +str(platoon_count))
            if platoon_count < 29 :
                if term == 'First Term':
    
                    if status == 'PENDING':
                        
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                
                        approved_by = approved_by,
                        date_declined = date_declined,
                        
                        
                        )
                        
                        return redirect('/cwts_admin_rejected')
                        
                    elif status == 'ENROLLED':
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                            middlename = middlename,
                            lastname=lastname,
                            email = email,
                            idnumber = idnumber,
                            address = address,
                            gender = gender,
                            age = age,
                            birthday = birthday,
                            section = section, 
                            cpnumber = cpnumber,
                            civil = civil,
                            nationality = nationality,
                            nfather = nfather,
                            foccupation = foccupation,
                            nmother = nmother,
                            moccupation = moccupation,
                            pcontact = pcontact,
                            nguardian = nguardian,
                            gcontact = gcontact,
                            sickness = sickness,
                            field = field,
                            platoons = platoons,
                            note = note,
                            status = status,
                            first_sem = first_sem,
                            second_sem = second_sem,
                            approved_by = approved_by,
                            date_declined = date_declined,
                        )
                        return redirect('/cwts_admin_rejected')
                        # return redirect(request.META['HTTP_REFERER'])
                    elif status == 'REJECTED':
                    
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                            middlename = middlename,
                            lastname=lastname,
                            email = email,
                            idnumber = idnumber,
                            address = address,
                            gender = gender,
                            age = age,
                            birthday = birthday,
                            section = section, 
                            cpnumber = cpnumber,
                            civil = civil,
                            nationality = nationality,
                            nfather = nfather,
                            foccupation = foccupation,
                            nmother = nmother,
                            moccupation = moccupation,
                            pcontact = pcontact,
                            nguardian = nguardian,
                            gcontact = gcontact,
                            sickness = sickness,
                            field = field,
                            platoons = platoons,
                            note = note,
                            status = status,
                            first_sem = status,
                            second_sem= second_sem,
                            approved_by = approved_by,
                            date_declined = date_declined,
                            
                        
                        )
                        
                        return redirect('/cwts_admin_rejected')
                
                elif term == 'Second Term':
                    
                    if status == 'PENDING':
                        
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                        middlename = middlename,
                        lastname=lastname,
                        email = email,
                        idnumber = idnumber,
                        address = address,
                        gender = gender,
                        age = age,
                        birthday = birthday,
                        section = section, 
                        cpnumber = cpnumber,
                        civil = civil,
                        nationality = nationality,
                        nfather = nfather,
                        foccupation = foccupation,
                        nmother = nmother,
                        moccupation = moccupation,
                        pcontact = pcontact,
                        nguardian = nguardian,
                        gcontact = gcontact,
                        sickness = sickness,
                        field = field,
                        platoons = platoons,
                        note = note,
                        status = status,
                
                        approved_by = approved_by,
                        date_declined = date_declined,
                        
                        
                        )
                        
                        return redirect('/admin_pending')
                        
                    elif status == 'ENROLLED':
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                            middlename = middlename,
                            lastname=lastname,
                            email = email,
                            idnumber = idnumber,
                            address = address,
                            gender = gender,
                            age = age,
                            birthday = birthday,
                            section = section, 
                            cpnumber = cpnumber,
                            civil = civil,
                            nationality = nationality,
                            nfather = nfather,
                            foccupation = foccupation,
                            nmother = nmother,
                            moccupation = moccupation,
                            pcontact = pcontact,
                            nguardian = nguardian,
                            gcontact = gcontact,
                            sickness = sickness,
                            field = field,
                            platoons = platoons,
                            note = note,
                            status = status,
                            first_sem = first_sem,
                            second_sem = second_sem,
                            approved_by = approved_by,
                            date_declined = date_declined,
                        )
                        return redirect('/admin_pending')
                        # return redirect(request.META['HTTP_REFERER'])
                    elif status == 'REJECTED':
                    
                        extenduser.objects.filter(id=ids).update(firstname = firstname,
                            middlename = middlename,
                            lastname=lastname,
                            email = email,
                            idnumber = idnumber,
                            address = address,
                            gender = gender,
                            age = age,
                            birthday = birthday,
                            section = section, 
                            cpnumber = cpnumber,
                            civil = civil,
                            nationality = nationality,
                            nfather = nfather,
                            foccupation = foccupation,
                            nmother = nmother,
                            moccupation = moccupation,
                            pcontact = pcontact,
                            nguardian = nguardian,
                            gcontact = gcontact,
                            sickness = sickness,
                            field = field,
                            platoons = platoons,
                            note = note,
                            status = status,
                            first_sem = first_sem,
                            second_sem= status,
                            approved_by = approved_by,
                            date_declined = date_declined,
                            
                        
                        )
                        
                        return redirect('/cwts_admin_rejected')
                return redirect('/cwts_admin_rejected')
                    
            else:
                messages.info(request,  str(platoons) + ' platoon has reached the maximum number of students')
                
            
            # return redirect('/manage_section')
                return redirect(request.META['HTTP_REFERER'])
    
    
def cwts_rejected_custom(request):
    if request.method == 'POST':
        try:
            sub = request.POST.get('subject')
            msg = request.POST.get('message')
            emaila = request.POST.get('rname')
            send_mail(sub, msg,'tupc.nstp@gmail.com',[emaila])
            print(sub)
            return redirect(request.META['HTTP_REFERER'])
            # return redirect('/admin_view_profile')

        except ImportError:
            messages.success(request, 'Email Encountered some errors. Please Contact your Administrator')
    return redirect('/cwts_admin_rejected')



def add_rotc_alumni(request):
    return render(request, 'activities/add_rotc_alumni.html')


def add_new_alumni(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        middle = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber = request.POST.get('idnumber')
        s_year = request.POST.get('s_year')
        note = request.POST.get('note')
        picture = '../nstpapp/static/images/tup.png'

        date_joined = datetime.datetime.now() 
         
        if User.objects.filter(username=idnumber).exists():
            messages.error(request, 'ID Number ' + str (idnumber) + ' Already Exist !')
            return redirect('/rotc_alumni')
        elif extenduser.objects.filter(email=email).exists():
            messages.error(request, 'Email ' + str (email) + ' Already Exist !')
            return redirect('/rotc_alumni')
       
        else:
            user = User.objects.create_user(username=idnumber,  email=email)
            datas = extenduser(s_year=s_year,firstname=firstname, middlename=middle, lastname=lastname, email=email, date_joined = date_joined,  idnumber=idnumber, field='ROTC', status='GRADUATE', picture=picture, note=note,user=user)
            datas.save()
        
            messages.error(request, 'Alumni  Aded successfully\n')
            # return redirect(request.META['HTTP_REFERER'])
            return redirect('/rotc_alumni')
    else:
        return redirect('/rotc_alumni')
    
    
    
def al_remove(request, id):
    extenduser.objects.filter(id=id).delete()
    User.objects.filter(id=id).delete()
    return redirect('/rotc_alumni')
    # return redirect('/admin_rejected')
    
    
def add_new_cwts_alumni(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        middle = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber = request.POST.get('idnumber')
        s_year = request.POST.get('s_year')
        note = request.POST.get('note')
        picture = '../nstpapp/static/images/tup.png'

        date_joined = datetime.datetime.now() 
         
        if User.objects.filter(username=idnumber).exists():
            messages.error(request, 'ID Number ' + str (idnumber) + ' Already Exist !')
            return redirect('/cwts_alumni')
        elif extenduser.objects.filter(email=email).exists():
            messages.error(request, 'Email ' + str (email) + ' Already Exist !')
            return redirect('/cwts_alumni')
       
        else:
            user = User.objects.create_user(username=idnumber,  email=email)
            datas = extenduser(s_year=s_year,firstname=firstname, middlename=middle, lastname=lastname, email=email, date_joined = date_joined,  idnumber=idnumber, field='CWTS', status='GRADUATE', picture=picture, note=note,user=user)
            datas.save()
        
            messages.error(request, 'Alumni  Aded successfully\n')
       
            return redirect('/cwts_alumni')
    else:
        return redirect('/cwts_alumni')
    
def al_cwts_remove(request, id):
    extenduser.objects.filter(id=id).delete()
    User.objects.filter(id=id).delete()
    messages.error(request, 'Deleted')
    return redirect('/cwts_alumni')
    # return redirect('/admin_rejected')
    
    
    
def add_alumni_years2(request):
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        combine = (start +"-"+ end)
        if alumni_school_year.objects.filter(years=combine).exists():
            messages.error(request, 'School year ' + str (combine) + ' Already Exist !')
            return redirect('/cwts_alumni')
        else:
            data1 = alumni_school_year(years=combine)
            data1.save()
    return redirect('/cwts_alumni')


def cwts_update_each_student(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        current_datetime = datetime.datetime.now() 
        print("sheesh" + str(ids))
        
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber= request.POST.get('idnumber')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        section = request.POST.get('section')
        cpnumber = request.POST.get('cpnumber')
        civil = request.POST.get('civil')
        nationality = request.POST.get('nationality')
        nfather = request.POST.get('nfather')
        foccupation = request.POST.get('foccupation')
        nmother = request.POST.get('nmother')
        moccupation = request.POST.get('moccupation')
        pcontact = request.POST.get('pcontact')
        nguardian = request.POST.get('nguardian')
        gcontact = request.POST.get('gcontact')
        sickness = request.POST.get('sickness')
        field = request.POST.get('field')
        platoons = request.POST.get('platoons')
        note = request.POST.get('note')
        status = request.POST.get('status')
        modified_by = request.POST.get('modified_by')
        

        if status == 'PENDING' or status == 'DROPPED' or status == 'GRADUATE' :
            
            extenduser.objects.filter(id=ids).update(firstname = firstname,
            middlename = middlename,
            lastname=lastname,
            email = email,
            idnumber = idnumber,
            address = address,
            gender = gender,
            age = age,
            birthday = birthday,
            section = section, 
            cpnumber = cpnumber,
            civil = civil,
            nationality = nationality,
            nfather = nfather,
            foccupation = foccupation,
            nmother = nmother,
            moccupation = moccupation,
            pcontact = pcontact,
            nguardian = nguardian,
            gcontact = gcontact,
            sickness = sickness,
            field = field,
            platoons = platoons,
            note = note,
            status = status,
            date_joined = current_datetime,
            modified_by = modified_by,
            date_modified = current_datetime,


         
            
            )
            
            return redirect('/manage_cwts_section')
            
        else:
            extenduser.objects.filter(id=ids).update(firstname = firstname,
                middlename = middlename,
                lastname=lastname,
                email = email,
                idnumber = idnumber,
                address = address,
                gender = gender,
                age = age,
                birthday = birthday,
                section = section, 
                cpnumber = cpnumber,
                civil = civil,
                nationality = nationality,
                nfather = nfather,
                foccupation = foccupation,
                nmother = nmother,
                moccupation = moccupation,
                pcontact = pcontact,
                nguardian = nguardian,
                gcontact = gcontact,
                sickness = sickness,
                field = field,
                platoons = platoons,
                note = note,
                status = status,
                date_joined = current_datetime,
                modified_by = modified_by,
                date_modified = current_datetime,
            )
        
        
    
    # return redirect('/manage_section')
        return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='/staff_signin')
def rotc_dropped(request):
    if request.user.is_staff:
    # pending = extenduser.objects.filter(status='PENDING').count()
        rejected = extenduser.objects.filter(status='DROPPED').filter(field = 'ROTC')

        context = {
        
            'rejected':rejected,
        
        }
        return render(request, 'activities/rotc_dropped.html', context)
    return redirect('/staff_signin')

@login_required(login_url='/staff_signin')
def cwts_dropped(request):
    if request.user.is_staff:
    
    # pending = extenduser.objects.filter(status='PENDING').count()
        rejected = extenduser.objects.filter(status='DROPPED').filter(field = 'CWTS')

        context = {
        
            'rejected':rejected,
        
        }
        return render(request, 'activities/cwts_dropped.html', context)

    return redirect('/staff_signin')


# all dropped data


def dropped_rotc_profile(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    section = sections.objects.all()
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id)
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1
    }
    

    
    return render(request, 'activities/rotc_dropped_profile.html', context)

def ro_drop_remove(request, id):
    extenduser.objects.filter(id=id).delete()
    User.objects.filter(id=id).delete()
    return redirect('/rotc_dropped')

def dropped_cwts_profile(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    section = sections.objects.all()
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id)
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1
    }
    

    
    return render(request, 'activities/cwts_dropped_profile.html', context)


def cw_drop_remove(request, id):
    extenduser.objects.filter(id=id).delete()
    User.objects.filter(id=id).delete()
    return redirect('/cwts_dropped')

def get_all(request):
    if request.method == 'POST':
        approved_by = request.POST.get('approved_by')
        first = request.POST.get('1st')
        second = request.POST.get('2nd')
        dropped = request.POST.get('dropped')
        graduate = request.POST.get('graduate')
        
        ids = request.POST.getlist('cbs')
        ids2 = request.POST.getlist('cbs2')
        ids3 = request.POST.getlist('cbs3')
        date_modified = datetime.datetime.now()
        
        if first is not None:
            for a in ids:
                extenduser.objects.filter(id=a).update(first_sem = first , second_sem='', status='', modified_by=approved_by, date_modified=date_modified)
                
        if second is not None:
            for a in ids2:
                extenduser.objects.filter(id=a).update(second_sem = second, modified_by=approved_by, date_modified=date_modified )
                
            # for first sem
        if dropped is not None:
            for a in ids:
                extenduser.objects.filter(id=a).update(status = dropped, first_sem=dropped , modified_by=approved_by, date_modified=date_modified )
            # for second sem
        if dropped is not None:
            for a in ids2:
                extenduser.objects.filter(id=a).update(status = dropped, second_sem=dropped , modified_by=approved_by, date_modified=date_modified )
                
    # end of dropping\
        if graduate is not None:
            for a in ids3:
                extenduser.objects.filter(id=a).update(status = graduate , modified_by=approved_by, date_modified=date_modified)
                
            
   
            
        return redirect('/manage_section')
    
def get_all2(request):
    if request.method == 'POST':
        approved_by = request.POST.get('approved_by')
        first = request.POST.get('1st')
        second = request.POST.get('2nd')
        dropped = request.POST.get('dropped')
        graduate = request.POST.get('graduate')
        
        ids = request.POST.getlist('cbs')
        ids2 = request.POST.getlist('cbs2')
        ids3 = request.POST.getlist('cbs3')
        date_modified = datetime.datetime.now()
        
        if first is not None:
            for a in ids:
                extenduser.objects.filter(id=a).update(first_sem = first , second_sem='', status='', modified_by=approved_by, date_modified=date_modified)
                
        if second is not None:
            for a in ids2:
                extenduser.objects.filter(id=a).update(second_sem = second, modified_by=approved_by, date_modified=date_modified )
                
            # for first sem
        if dropped is not None:
            for a in ids:
                extenduser.objects.filter(id=a).update(status = dropped, first_sem=dropped , modified_by=approved_by, date_modified=date_modified )
            # for second sem
        if dropped is not None:
            for a in ids2:
                extenduser.objects.filter(id=a).update(status = dropped, second_sem=dropped , modified_by=approved_by, date_modified=date_modified )
                
    # end of dropping\
        if graduate is not None:
            for a in ids3:
                extenduser.objects.filter(id=a).update(status = graduate , modified_by=approved_by, date_modified=date_modified)
   
            
        return redirect('/manage_cwts_section')
    
    
def staff(request):
    return render(request, 'activities/staff.html')

def staff_login(request):
    return render(request, 'activities/staff_login.html')

def staff_signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        middle = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber = request.POST.get('idnumber')
        password = request.POST.get('password1')
        picture = request.FILES['picture']
        s_year = request.POST.get('s_year')
        field = request.POST.get('field')
        date_joined = datetime.datetime.now()  
        if User.objects.filter(username=idnumber).exists():
            messages.error(request, 'ID Number ' + str (idnumber) + ' Already Exist !')
            return redirect('/staff')
        elif extenduser.objects.filter(email=email).exists():
            messages.error(request, 'Email ' + str (email) + ' Already Exist !')
            return redirect('/staff')
       
        else:
            user = User.objects.create_user(username=idnumber, password=password, email=email, first_name=firstname, last_name=lastname)
            datas = extenduser(s_year=s_year,firstname=firstname, middlename=middle, lastname=lastname, email=email, date_joined = date_joined,  idnumber=idnumber,picture=picture, category = 'STAFF', field=field,user=user)
            datas.save()
            auth.login(request, user)
            messages.error(request, 'Account created successfully\nPlease Login and complete profile for verification. Thank you')
            return redirect('/staff_login')
    else:
        return redirect('/staff')
    
    # we will use this as login url
def staff_signin(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                user = authenticate(username=username, password=password)
                if user is not None and user.is_staff:
                    auth.login(request, user)
                    return redirect('/admin_dashboard')
                else:
                    messages.error(request, 'Invalid username or password')
                    return redirect('/staff_login')
            else:
                messages.error(request, 'ID Number ' + str (username) + ' Does not exist !')
                return redirect('/staff_login')
    else:
        messages.error(request, 'Invalid username or password !')
        return redirect('/staff_login')
    
def admin1(request):
    return render(request, 'activities/admin_ui.html')


def enrollment(request):
    name = extenduser.objects.filter(user = request.user)
    sy = school_year.objects.all()
    context = {
        'name': name,
        'sy':[sy.last()]

    }
    return render(request, 'activities/enrollment.html', context)

def renew_enroll(request,idnumber):
    if request.method == 'POST':
        idnumber = request.POST.get('idnumber')
        extenduser.objects.filter(idnumber=idnumber).update(second_sem='PENDING', status='PENDING')
        messages.error(request, 'Enrollment Request Submitted')
    return redirect('/enrollment')

def enroll_first(request,idnumber):
    if request.method == 'POST':
        idnumber = request.POST.get('idnumber')
        extenduser.objects.filter(idnumber=idnumber).update(first_sem='PENDING', status='PENDING')
        messages.error(request, 'Enrollment Request Submitted')
    return redirect('/enrollment')



def ro_enrolled(request):
    approved = extenduser.objects.filter(status='ENROLLED', field='ROTC')
    total = extenduser.objects.filter(status='ENROLLED', field='ROTC').count()
    context = {
        'approved':approved,
        'total':total
    }
    return render(request, 'activities/ro_enrolled.html', context)

def enrolled_profile(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    section =  sections.objects.filter(fiel = 'ROTC')
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id).filter(status='ENROLLED')
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1
    }
    

    
    return render(request, 'activities/enrolled_profile.html', context)

def update_enrolled_student(request):
    if request.method == 'POST':
        ids = request.POST.get('ids')
        current_datetime = datetime.datetime.now() 
        print("sheesh" + str(ids))
        
        firstname = request.POST.get('firstname')
        middlename = request.POST.get('middlename')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber= request.POST.get('idnumber')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        section = request.POST.get('section')
        cpnumber = request.POST.get('cpnumber')
        civil = request.POST.get('civil')
        nationality = request.POST.get('nationality')
        nfather = request.POST.get('nfather')
        foccupation = request.POST.get('foccupation')
        nmother = request.POST.get('nmother')
        moccupation = request.POST.get('moccupation')
        pcontact = request.POST.get('pcontact')
        nguardian = request.POST.get('nguardian')
        gcontact = request.POST.get('gcontact')
        sickness = request.POST.get('sickness')
        field = request.POST.get('field')
        platoons = request.POST.get('platoons')
        note = request.POST.get('note')
        status = request.POST.get('status')
        modified_by = request.POST.get('modified_by')
        

        if status == 'PENDING' or status == 'DROPPED' or status == 'GRADUATE' :
            
            extenduser.objects.filter(id=ids).update(firstname = firstname,
            middlename = middlename,
            lastname=lastname,
            email = email,
            idnumber = idnumber,
            address = address,
            gender = gender,
            age = age,
            birthday = birthday,
            section = section, 
            cpnumber = cpnumber,
            civil = civil,
            nationality = nationality,
            nfather = nfather,
            foccupation = foccupation,
            nmother = nmother,
            moccupation = moccupation,
            pcontact = pcontact,
            nguardian = nguardian,
            gcontact = gcontact,
            sickness = sickness,
            field = field,
            platoons = platoons,
            note = note,
            status = status,
            date_joined = current_datetime,
            modified_by = modified_by,
            date_modified = current_datetime,


         
            
            )
            
            return redirect('/ro_enrolled')
            
        else:
            extenduser.objects.filter(id=ids).update(firstname = firstname,
                middlename = middlename,
                lastname=lastname,
                email = email,
                idnumber = idnumber,
                address = address,
                gender = gender,
                age = age,
                birthday = birthday,
                section = section, 
                cpnumber = cpnumber,
                civil = civil,
                nationality = nationality,
                nfather = nfather,
                foccupation = foccupation,
                nmother = nmother,
                moccupation = moccupation,
                pcontact = pcontact,
                nguardian = nguardian,
                gcontact = gcontact,
                sickness = sickness,
                field = field,
                platoons = platoons,
                note = note,
                status = status,
                date_joined = current_datetime,
                modified_by = modified_by,
                date_modified = current_datetime,
            )
        
        
    
    # return redirect('/manage_section')
        return redirect(request.META['HTTP_REFERER'])


def cw_enrolled(request):
    approved = extenduser.objects.filter(status='ENROLLED', field='CWTS')
    total = extenduser.objects.filter(status='ENROLLED', field='CWTS').count()
    context = {
        'approved':approved,
        'total':total
    }
    return render(request, 'activities/cw_enrolled.html', context)



def cw_enrolled_profile(request, id):
    ids= request.POST.get('ids')
    labels = [ 'ABSENT','PRESENT']
    present = []
    absent = []
    name = extenduser.objects.filter(id=id)
    pres1 = extenduser.objects.filter(id=id)
    abs1 = extenduser.objects.filter(id = id)
    section =  sections.objects.filter(fiel = 'CWTS')
    
    print(ids)
    getSection = request.POST.get('getSection')
    details = extenduser.objects.filter(id=id).filter(status='ENROLLED')
    for s in pres1:
        present.append(s.pres1)
       
    for k in abs1:
        absent.append(k.abs1)
    context = {
        'ids': ids,
        'getSection': getSection,
        'details': details,
        'section': section,
        'labels': labels,
        'present': present,
        'absent': absent,
        'name': name,
        'pres1':pres1,
        'abs1':abs1
    }
    

    
    return render(request, 'activities/cw_enrolled_profile.html', context)
