from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

#models imported
from .models import extenduser

# Create your views here.



#   PAGE SHOWING
def index(request):
    return render(request, 'activities/index.html')
def signup_page(request):
    return render(request, 'activities/signup.html')
def login_page(request):
    return render(request, 'activities/login.html')
def dashboard_page(request):
    name = extenduser.objects.filter(user = request.user)
    context = {
        'name': name,
    }
    return render(request, 'activities/dashboard.html', context)
def profile_page(request):
    return render(request, 'activities/profile.html')
def editprofile(request):
    return render(request, 'activities/editprofile.html')







def navbar(request):
    return render(request, 'activities/navbar.html')

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
        
        if User.objects.filter(username=idnumber).exists():
            messages.error(request, 'ID Number ' + str (idnumber) + ' Already Exist !')
            return redirect('/signup_page')
        elif extenduser.objects.filter(email=email).exists():
            messages.error(request, 'Email ' + str (email) + ' Already Exist !')
            return redirect('/signup_page')
        else:
            user = User.objects.create_user(username=idnumber, password=password,)
            datas = extenduser(firstname=firstname, middlename=middle, lastname=lastname, email=email, idnumber=idnumber, password=password,user=user)
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
            user = authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/dashboard_page')
            else:
                messages.error(request, 'Invalid username or password')
                return redirect('/login_page')
    else:
        messages.error(request, 'Invalid username or password')
        return redirect('/login_page')