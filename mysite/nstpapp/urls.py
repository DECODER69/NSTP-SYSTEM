from django.urls import path
from . import views
from django.conf.urls import static
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.urls import include, re_path

# password reset
from django.contrib.auth import views as auth_views


app_name = 'activities'

urlpatterns = [
    path('', views.index, name='index'),
    path('navbar/', views.navbar, name='navbar'),
    path('logout_student/', views.logout_student, name='logout_student'),
    path('signup_page/', views.signup_page, name='signup_page'),
    path('signup/', views.signup, name='signup'),
    path('login_page/',views.login_page, name='login_page'),
    path('signin/', views.signin, name='signin'),
    path('dashboard_page/', views.dashboard_page, name='dashboard_page'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('edit/', views.edit, name='edit'),
    path('others/', views.others, name='others'),
    path('edit_others/<str:id>', views.edit_others, name='edit_others'),
    path('health/', views.health, name='health'),
    path('edit_health/<str:id>', views.edit_health, name='edit_health'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)