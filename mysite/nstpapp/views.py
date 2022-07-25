from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages 

#models imported
from .models import extenduser

# Create your views here.



#   PAGE SHOWING
def index(request):
    return render(request, 'activities/index.html')
def signup_page(request):
    return render(request, 'activities/signup.html')

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