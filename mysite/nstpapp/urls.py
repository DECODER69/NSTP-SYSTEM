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

from django.urls import reverse_lazy

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
    path('approve/<str:idnumber>', views.approve, name='approve'),
    path('decline/<str:id>', views.decline, name='decline'),
    path('admin_rejected/', views.admin_rejected, name='admin_rejected,'),
    path('custom/', views.custom, name='custom'),
    path('rejected_email_page/<str:id>', views.rejected_email_page, name='rejected_email_page'),
    path('school_years/', views.school_years, name='school_years'),
    path('create_sy/', views.create_sy, name='create_sy'),
    # path('allumni_page/', views.allumni_page, name='allumni_page'),
    path('allumni_content/', views.allumni_content, name='allumni_content'),
    path('delete_sy/<str:id>', views.delete_sy, name='delete_sy'),
    path('create_platoon_page/', views.create_platoon_page, name='create_platoon_page'),
    path('create_section/', views.create_section, name='create_section'),
    path('counts/', views.counts, name='counts'),
    path('pl_content/', views.pl_content, name='pl_content'),
    path('section_content/', views.section_content, name='section_content'),
    path('view_images/<str:id>', views.view_images, name='view_images'),
    path('create_platoon_page2/', views.create_platoon_page2, name='create_platoon_page2'),
    path('manage_section/', views.manage_section, name='manage_section'),
    path('edit_manage/<str:id>', views.edit_manage, name='edit_manage'),
    path('export/', views.export, name='export'),
    path('edit_student/<str:id>', views.edit_student, name='edit_student'),
    path('attendance_page/', views.attendance_page, name='attendance_page'),
    path('create_day/',views.create_day, name='create_day'),
    path('create_annoucement/', views.create_announcement, name='create_announcement'),
    path('edit_announcement/<str:id>', views.edit_announcement, name='edit_announcement'),
    path('delete_announcement/<str:id>', views.delete_announcement, name='delete_announcement'),
    path('attendance_sections/', views.attendance_sections, name='attendance_sections'),
    path('attendance_main/', views.attendance_main, name='attendance_main'),
    path('attendance_main_page/', views.attendance_main_page, name='attendance_main_page'),
    # path('record/<str:id>', views.record, name='record'),
    path('update_attendance/', views.update_attendance, name='update_attendance'),
    path('add_students/', views.add_students, name='add_students'),
    path('assign_section/', views.assign_section, name='assign_section'),
    path('update_sy/', views.update_sy, name='update_sy'),
    # password resets
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='activities/registration/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='activities/registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='activities/registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='activities/registration/password_reset_complete.html'),name='password_reset_complete'),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)