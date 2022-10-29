from dataclasses import field
import csv
from distutils.command.build_scripts import first_line_re
from genericpath import exists

from pkgutil import extend_path
from django.db.models import Sum
import re
from subprocess import IDLE_PRIORITY_CLASS
from turtle import end_fill
from webbrowser import get
from django.http import HttpResponseRedirect
from django.http.request import QueryDict


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
from .models import activity, extenduser,school_year, sections, training_day,Announcement, certification, activity, midterm, finals
import os
import csv  

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
    return render(request, 'activities/landing.html')
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
    name = extenduser.objects.filter(user = request.user)
    context = {
        'name': name,
    }
    return render(request, 'activities/dashboard.html', context)
@login_required(login_url='/login_page')
def profile_page(request):
    details = extenduser.objects.filter(user=request.user)
    context={
        'details':details,
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
@login_required(login_url='/login_page')
def health(request):
    uwus = extenduser.objects.filter(user=request.user)
    context = {
        'uwus':uwus,
    }
    return render(request, 'activities/health.html', context)

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

def admin_dashboard(request):
    audience = sections.objects.all()
    ann = Announcement.objects.all()
    sy = school_year.objects.all()
    active = extenduser.objects.filter(status='ENROLLED').count()
    pending = extenduser.objects.filter(status='PENDING').count()

    context = {
        'active':active,   
        'pending':pending,
        'sy':[sy.last()],
        'audience':audience,
        'ann':ann,
    
    }
    return render(request, 'activities/admin_dashboard.html', context)

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
    pending = extenduser.objects.filter(status='PENDING').count()
    pendings = extenduser.objects.filter(status='PENDING')
    context = {
        'pendings':pendings,
        'pending':pending,
        'platoons':platoons
    }
    return render(request, 'activities/admin_pending.html', context)

def admin_rejected(request):
    # pending = extenduser.objects.filter(status='PENDING').count()
    rejected = extenduser.objects.filter(status='REJECTED')

    context = {
      
        'rejected':rejected,
       
    }
    return render(request, 'activities/admin_rejected.html', context)

def admin_view_profile(request, id):
    profiles = extenduser.objects.filter(id=id)
    pending = extenduser.objects.filter(status='PENDING').count()
    context = {
        'profiles':profiles,
        'pending':pending
    }
    return render(request, 'activities/profile_view.html', context)
 


def school_years(request):

    s_years = school_year.objects.all()
    ss_years = extenduser.objects.all()
    ewan = school_year.objects.all()
   
    context = {
        'ewan':ewan,
        's_years':[s_years.last()],
        'ss_years':ss_years,
        # 'graduates':graduates
        
    }

    return render(request, 'activities/sy.html', context)

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

def manage_section(request):
    current_datetime = datetime.datetime.now() 
    userContent = User.objects.all()
    sectionxx = extenduser.objects.all()
    counts = extenduser.objects.filter(status='ENROLLED').count()
    counts1 = extenduser.objects.filter(status='ENROLLED')
    section = sections.objects.all()
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
  






# MALI ITOOO

def attendance_main_page(request):
    return render(request, 'activities/attendance_main.html')


# eof mali




#   EOF PAGE SHOWING

# functions

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        middle = request.POST.get('middle')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        idnumber = request.POST.get('idnumber')
        password = request.POST.get('password1')
        picture = request.FILES['picture']
        s_year = request.POST.get('s_year')
        if User.objects.filter(username=idnumber).exists():
            messages.error(request, 'ID Number ' + str (idnumber) + ' Already Exist !')
            return redirect('/signup_page')
        elif extenduser.objects.filter(email=email).exists():
            messages.error(request, 'Email ' + str (email) + ' Already Exist !')
            return redirect('/signup_page')
       
        else:
            user = User.objects.create_user(username=idnumber, password=password, email=email)
            datas = extenduser(s_year=s_year,firstname=firstname, middlename=middle, lastname=lastname, email=email, idnumber=idnumber, password=password,picture=picture,user=user)
            datas.save()
            auth.login(request, user)
            messages.info(request, 'Account created successfully\nPlease Login and complete profile for verification')
            return redirect('/signup_page')
    else:
        return redirect('/')


def signin(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            if User.objects.filter(username=username).exists():
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('/dashboard_page')
                else:
                    messages.error(request, 'Incorrect password')
                    return redirect('/login_page')
            else:
                messages.error(request, 'ID Number ' + str (username) + ' Does not exist !')
                return redirect('/login_page')
    else:
        messages.error(request, 'Invalid username or password !')
        return redirect('/login_page')

@login_required(login_url='/login_page')
def edit(request):

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
        return redirect('/others')
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

@login_required(login_url='/login_page')
def edit_health(request, id):
    hehes = extenduser.objects.get(id=id)
    if request.method == 'POST':
        proof = request.FILES['prof']
        if proof is not None:
            proof_path = proof.path
            if os.path.exists(proof_path):
                os.remove(proof_path)
                disease = request.POST.getlist('check')
                specific = request.POST.get('spec')
                hehes=extenduser(disease=disease, specific=specific)
                hehes.save()
                return redirect('/health')
            else:
                disease = request.POST.getlist('check')
                specific = request.POST.get('spec')
                hehes=extenduser(disease=disease, specific=specific)
                hehes.save()
                return redirect('/health')
    else:
        print("DONE")
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
    

    extenduser.objects.filter(idnumber=stat2).update(status='ENROLLED', platoons=platoons)
    messages.success(request, 'Student ' + str (stat2) + ' has been Approved !')
    return redirect('/admin_pending')

def decline(request, id):
   
    stat2 = request.POST.get('getID2')
   
    print(stat2)
    extenduser.objects.filter(idnumber=stat2).update(status='REJECTED')
    messages.success(request, 'Student ' + str (stat2) + ' has been Rejected !')
    return redirect('/admin_pending')

def r_approve(request, idnumber):
    stat2 = request.POST.get('getID')
    platoons = request.POST.get('platoons')
    

    extenduser.objects.filter(idnumber=stat2).update(status='ENROLLED', platoons=platoons)
    messages.success(request, 'Student ' + str (stat2) + ' has been Approved !')
    return redirect('/admin_rejected')

def r_decline(request, id):
   
    stat2 = request.POST.get('getID2')
   
    print(stat2)
    extenduser.objects.filter(idnumber=stat2).update(status='REJECTED')
    messages.success(request, 'Student ' + str (stat2) + ' has been Rejected !')
    return redirect('/admin_rejected')



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
        
def create_sy(request):
    if request.method == 'POST':
        yearsz = request.POST.get('year')
        if school_year.objects.filter(years=yearsz).exists():
            messages.info(request, 'School year ' + str (yearsz) + ' ALready exist !')
            return redirect('/school_years')
        else:
            data = school_year(years=yearsz)
            data.save()
            messages.success(request, 'School year ' + str (yearsz) + ' Successfully Created !')
            return redirect('/school_years')
    return redirect('/school_years')

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




def delete_sy(request, id):
    school_year.objects.filter(id=id).delete()
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
    
    



def section_content(request):
    userContent = User.objects.all()
    schools = school_year.objects.all()
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
         
    }
    print(content33)
    print(getSection)
    return render(request, 'activities/pl_content.html', context)

def download(request):
    if request.method == 'POST':
    
        csvfile = extenduser.objects.filter(status='ENROLLED')
        response = HttpResponse(content_type='text/csv')  
        print("CSV FILE ITO" + str(csvfile))
        
        response['Content-Disposition'] = 'attachment; filename="List.csv"  '
        writer = csv.writer(response)  
        writer.writerow(['STUDENT NUMBER', 'FIRSTNAME', 'LASTNAME', 'NSTP COMPONENT', 'NSTP SECTION', 'STATUS'])  
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

def add_students(request):
    if request.method == 'POST':
        platoon = request.POST.get('platoon')
        allstudent = extenduser.objects.filter(status='ENROLLED').filter(platoons='')
    else:
        return redirect('/manage_section')
    context = {
        'allstudent':allstudent,
        'platoon':platoon
    }
    return render(request, 'activities/students_list.html', context)

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
    return render(request, 'activities/certificate_page.html', context)

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
        namess = extenduser.objects.filter(s_year=years).filter(status='GRADUATE')
        print(section)
        print("pogi"+str(years))
        
        context = {
            'yyy':yyy,
            'sys1':sys1,
            'namess':namess,
            'details':[details.last()],
            
        }
        return render(request, 'activities/certificate.html', context)
    
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

def update_acts(request):
    if request.method == 'POST':
        current_datetime = datetime.datetime.now() 
        ids= request.POST.get('ids')
        print("hahahaha" + str(ids))
        school_year.objects.filter(years=ids).update(acts='DONE', date_generated=current_datetime)
        print("hahahaha" + str(ids))
        return redirect('/cert_page')
        
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
    counts = extenduser.objects.filter(status='DROP').count()
    counts1 = extenduser.objects.filter(status='DROP')
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


def alumni_page(request):
    school_years = school_year.objects.all()
    context = {
        'school_years':school_years
    }
    return render(request, 'activities/allumni.html', context)


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

def sample_attendance(request):

    section = sections.objects.all()
    date = training_day.objects.all()

    context = {
        'date':date, 
        'section':section,
    }

    return render(request, 'activities/sample_attendance.html', context)

def show_students(request):
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
    section = sections.objects.all()
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
        td_count = request.POST.get('td_count')
        ids = request.POST.getlist('id4')
        id2 = request.POST.getlist('id2')
        
        date1 = request.POST.get('check1')
        date0 = request.POST.get('check0')
        # print("date 0 ito " +str(date0))
        # print("date 1 ito " +str(date1))
        print("td count ito "+str(td_count))

        if td_count == str(1):
            if ids:
                for i in ids:
                    print("present date 0 "+str(i))
                    extenduser.objects.filter(id=i).update(TD1='1')
            if id2:
                for j in id2:
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
                    
                    # absents

                    
        # if date1 == 'None':
        #     if td_count == str(1):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD1=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD1='ABSENT')
        #     elif td_count == str(2):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD2=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD2='ABSENT')
        #     elif td_count == str(3):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD3=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD3='ABSENT')
        #     elif td_count == str(4):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD4=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD4='ABSENT')
        #     elif td_count == str(5):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD5=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD5='ABSENT')
        #     elif td_count == str(6):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD6=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD6='ABSENT')
        #     elif td_count == str(7):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD7=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD7='ABSENT')
        #     elif td_count == str(8):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD8=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD8='ABSENT')
        #     elif td_count == str(9):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD9=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD9='ABSENT')
        #     elif td_count == str(10):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD10=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD10='ABSENT')
        #     elif td_count == str(11):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD11=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD11='ABSENT')
        #     elif td_count == str(12):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD12=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD12='ABSENT')
        #     elif td_count == str(13):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD13=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD13='ABSENT')
        #     elif td_count == str(14):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD14=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD14='ABSENT')
        #     elif td_count == str(15):
        #         if ids:
        #             for i in ids:
        #                 print("present date 0 "+str(i))
        #                 extenduser.objects.filter(id=i).update(TD15=date0)
        #         if id2:
        #             for j in id2:
        #                 print("absent date 0 "+str(j))
        #                 extenduser.objects.filter(id=j).update(TD15='ABSENT')

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
        ids = request.POST.getlist('getId')
        credits = request.POST.getlist('credits')
        print("creds "+ str(credits))
        print("ids"+ str(ids))
        
        for i, j in zip(ids, credits):
            print("id" + str(i), "creds"+ str(j))
            extenduser.objects.filter(id=i).update(att_credits=j)
        # extenduser.objects.filter
    return redirect('/sample_attendance')
def grades(request):
    acts = activity.objects.all()
    section = sections.objects.all()
    context = {
        'section':section, 
        'acts': acts
    }
    return render(request, 'activities/grades.html', context)

def modify_grades(request):
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
        for a, b, c, d , e, f , i in zip(act1, act2, act3, act4, act5, act6,  ids ):
            # extenduser.objects.filter(id=i).update(act1=a, act2=b, act3=c,act4=d, act5=e, act6=f)
            print("hahaha "+ a, b, c, d , e, f)
            
        for a2, b2, c2, d2 , e2, f2, i2 in zip( act1_2, act2_2, act3_2, act4_2, act5_2, act6_2,  ids_2):
            extenduser.objects.filter(id=i2).update(act1_2=a2, act2_2=b2, act3_2=c2, act4_2=d2, act5_2=e2, act6_2=f2)
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
    section2 = sections.objects.all()
    context = {
        'section2':section2,
        'acts2': acts2,
    }
    return render(request, 'activities/attendance_tab.html', context)

def midterms(request):
    acts3 = midterm.objects.all()
    section2 = sections.objects.all()
    context = {
        'section2':section2,
        'acts3': acts3,
    }
    return render(request, 'activities/midterm.html', context)


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

def finals_(request):
    acts3 = finals.objects.all()
    section2 = sections.objects.all()
    context = {
        'section2':section2,
        'acts3': acts3,
    }
    return render(request, 'activities/finals.html', context)


def modify_finals(request):
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
def final_grade(request):
    acts3 = finals.objects.all()
    section2 = sections.objects.all()
    context = {
        'section2':section2,
        'acts3': acts3,
    }
    return render(request, 'activities/final_grade.html', context)

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
            print(a, b, c)
        for  d, e, f in zip(ids_2, second_grade, equivalent2):
            print(d, e, f)
            extenduser.objects.filter(id=d).update(final_grade_2=e, second_equivalents=f)
        return redirect('/final_grade')
