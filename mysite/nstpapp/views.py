from dataclasses import field
import csv
from pkgutil import extend_path
from django.http import HttpResponseRedirect

import xlwt
from http.client import HTTPResponse
from multiprocessing import context
from pickle import FALSE
from re import S
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
from .models import extenduser,school_year, sections, training_day,Announcement
import os


# emails
from django.core.mail import send_mail
from django.db import IntegrityError

# Create your views here.

# track active users
from django.utils.timezone import now
from datetime import timedelta



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
    
    details = extenduser.objects.filter(status='ENROLLED').order_by('field')
    pendings = extenduser.objects.filter(status='PENDING')
    pending = extenduser.objects.filter(status='PENDING').count()

    context = {
        'pending':pending,
        'details': details,
        'pendings':pendings,
       
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

def pl_content(request):
    return render(request, 'activities/pl_content.html')


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
  
     
def attendance_page(request):
    days = training_day.objects.all()
    day_count = training_day.objects.all().count()
    context = {
        'days':days,
        'day_count':day_count
    }
    return render(request, 'activities/attendance_page.html', context)





# MALI ITOOO

def attendance_main_page(request):
    return render(request, 'activities/attendance_main.html')


# eof mali




#   EOF PAGE SHOWING

# functions

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('fistname')
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
            messages.info(request, 'Account created successfully')
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
        hehes.proof = request.FILES['proof']
        proof_path = hehes.proof.path
        if os.path.exists(proof_path):
            os.remove(proof_path)
            hehes.disease = request.POST.getlist('check')
            hehes.specific = request.POST.get('spec')
            hehes.save()
            return redirect('/health')

        hehes.disease = request.POST.getlist('check')
        hehes.specific = request.POST.get('spec')
        hehes.save()
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
        sub = request.POST.get('emailtext')
        msg = request.POST.get('message')
        emaila = request.POST.get('cusemail')
        send_mail(sub, msg,'tupc.nstp@gmail.com',[emaila])
        return redirect('/admin_rejected')
    return redirect('/admin_rejected')\
        
def create_sy(request):
    if request.method == 'POST':
        years = request.POST.get('year')
        if school_year.objects.filter(years=years).exists():
                messages.info(request, 'School year ' + str (years) + ' ALready exist !')
                return redirect('/school_years')
        else:
            data = school_year(years=years)
            data.save()
            messages.success(request, 'School year ' + str (years) + ' Successfully Created !')
            return redirect('/school_years')
    return redirect('/school_years')

def allumni_content(request):
    if request.method == 'POST':
        getYear = request.POST.get('getYear')
        content = extenduser.objects.filter(s_year=getYear).filter(status='GRADUATE')
        content2 = extenduser.objects.filter(s_year=getYear).count()
    else:
        print("hahahahaaha")
        return render(request, 'activities/allumni.html')
    context = {
        'content':content,
        'content2':content2
    }
    print(getYear)


    return render(request, 'activities/allumni.html', context)


def delete_sy(request, years):
    if request.method == 'POST':
        yrid = request.POST.get('getID2')
        syid = school_year.objects.filter(years=yrid).delete()
        context = {
            'syid':syid,
        }
        messages.success(request, 'School year ' + str (yrid) + ' Successfully Removed !')
        return redirect('/school_years', context)

def create_section(request):
    if request.method == 'POST':
        secs = request.POST.get('secs')
        if secs is not None:
            if sections.objects.filter(section_created  = secs).exists():
                messages.info(request, 'Section ' + str (secs) + ' Already exist !')
                return redirect('/manage_section')
            else:
                data = sections(section_created=secs)
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
    return render (request, 'activities/edit_manage.html', context)



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
        content3 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        content33 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED').count()
    else:
        print("hahahahaaha")
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


def create_day(request):
    if request.method == 'POST':
        day = request.POST.get('day')
        title = request.POST.get('title')
        if day is not None:
            if training_day.objects .filter(title=title).exists():
                messages.info(request, (title) + ' Already exist !')
                return redirect('/attendance_page')
    
            else:
                data = training_day(day_created=day, title=title)
                data.save()
                messages.info(request, (title) + ' Created !')
                return redirect('/attendance_page')
        else:
            messages.info(request, 'Please Input Something!! Ex: ALPHA')
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

def attendance_sections(request):
    platoons = sections.objects.all()
    context = {
        'platoons':platoons
    }
    return render(request, 'activities/attendance_section.html', context)


def attendance_main(request):
    schools = school_year.objects.all()
    if request.method == 'POST':


        
        getSection = request.POST.get('getSection')
        


        sectionx = sections.objects.all()
        content3 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED')
        content33 = extenduser.objects.filter(platoons=getSection).filter(status='ENROLLED').count()
     

        
        
    else:
        return redirect('/attendance_sections')
    context = {
        'content3':content3,
        'content33':content33,
        'getSection':getSection,
        'schools':[schools.last()],
        'sectionx':sectionx
    }
    return render(request, 'activities/attendance_main.html', context)
  

def record(request):
    if request.method == 'POST':
        pass
    return redirect('/attendance_main')
