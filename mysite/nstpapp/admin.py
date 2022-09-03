from django.contrib import admin

from django.contrib import admin
from .models import extenduser, school_year, training_day

# Register your models here.

admin.site.register(extenduser)
admin.site.register(school_year)
admin.site.register(training_day)



