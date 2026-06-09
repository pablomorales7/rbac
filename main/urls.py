# RBAC/urls.py

from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    # Signup and Login
    path('signup/', views.signup, name='signup'),
    path('', views.universal_login, name='login'),

    # Dashboard for each role
    path('admin-dashboard/', views.admin_dashboard, name='admin_page'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_page'),
    path('student-dashboard/', views.student_dashboard, name='student_page'),
    

    path('makerole/', views.makerole, name='makerole'),


    
]
