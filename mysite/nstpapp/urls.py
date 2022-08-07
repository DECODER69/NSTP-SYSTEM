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
    path('admin_nav/', views.admin_nav, name='admin_nav'),
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
    path('file_manager/', views.file_manager, name='file_manager'),
    path('files_rotc/', views.files_rotc, name='files_rotc'),
    path('rotc_files/', views.rotc_files, name='rotc_files'),
    path('files_cwts/', views.files_cwts, name='files_cwts'),
    path('cwts_files/', views.cwts_files, name='cwts_files'),
    path('fields/', views.fields, name='fields'),
    path('field_rotc/', views.field_rotc, name='field_rotc'),
    
    
    
    # admin urls
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_staff/', views.admin_staff, name='admin_staff'),
    path('admin_pending/', views.admin_pending, name='admin_pending'),
    path('admin_view_profile/<str:id>', views.admin_view_profile, name='admin_view_profile'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)