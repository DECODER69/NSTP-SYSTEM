from dataclasses import field
from multiprocessing import context
from pickle import FALSE
from tabnanny import check
from tkinter import FLAT
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

#models imported
from .models import extenduser, sy
import os


# emails
from django.core.mail import send_mail

# Create your views here.



#   PAGE SHOWING
def index(request):
    return render(request, 'activities/index.html')
def signup_page(request):
    return render(request, 'activities/signup.html')
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
        'pending':pending
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
    active = extenduser.objects.filter(status='ENROLLED').count()
    pending = extenduser.objects.filter(status='PENDING').count()
    context = {
        'active':active,   
        'pending':pending,
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
    pending = extenduser.objects.filter(status='PENDING').count()
    pendings = extenduser.objects.filter(status='PENDING')
    context = {
        'pendings':pendings,
        'pending':pending
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
    years = sy.objects.all()
    context = {
        'years':years
    }
    return render(request, 'activities/sy.html', context)




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
        
        if User.objects.filter(username=idnumber).exists():
            messages.error(request, 'ID Number ' + str (idnumber) + ' Already Exist !')
            return redirect('/signup_page')
        elif extenduser.objects.filter(email=email).exists():
            messages.error(request, 'Email ' + str (email) + ' Already Exist !')
            return redirect('/signup_page')
        else:
            user = User.objects.create_user(username=idnumber, password=password,)
            datas = extenduser(firstname=firstname, middlename=middle, lastname=lastname, email=email, idnumber=idnumber, password=password,picture=picture,user=user)
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

def approve(request, id):
    stat2 = request.POST.get('getID')
    name = extenduser.objects.all()
    name.idnumber = extenduser.objects.filter(id=stat2)
    # for names in name.idnumber:
        
    # print(name.idnumber[0] )
    extenduser.objects.filter(id=stat2).update(status='ENROLLED')
    messages.success(request, 'Student ' + str (name.idnumber[0]) + ' has been Approved !')
    return redirect('/admin_pending')

def decline(request, id):
   
    stat2 = request.POST.get('getID2')
    print(stat2)
    extenduser.objects.filter(id=stat2).update(status='REJECTED')
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
        pass
        
    return redirect('/school_years')
