from django.shortcuts import render

#models imported
from .models import extenduser

# Create your views here.



#   PAGE SHOWING
def index(request):
    return render(request, 'activities/index.html')
def signup_page(request):
    return render(request, 'activities/signup.html')

#   EOF PAGE SHOWING

