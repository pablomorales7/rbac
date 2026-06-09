# main/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.http import HttpResponse
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse
from .models import UserProfile
from .decorators import allowed_roles

# ----------- Admin Signup View -----------

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email    = request.POST.get('email')
        phone    = request.POST.get('phone')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already taken!")

        user = User.objects.create_user(username=username, email=email, password=password)
        profile = UserProfile.objects.create(
            user=user,
            role='student',
            #role='admin',
            phone=phone,
            signup_time=timezone.now()
        )

        login(request, user)
        return redirect('student_page')

    return render(request, 'signup.html')

# ----------- Universal Login View -----------

def universal_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            try:
                profile = UserProfile.objects.get(user=user)
                role = profile.role

                if role == 'admin':
                    return redirect('admin_page')

                elif role == 'teacher':
                    return redirect('teacher_page')

                elif role == 'student':
                    return redirect('student_page')
                else:
                    return HttpResponse("Unknown role!")
            except UserProfile.DoesNotExist:
                return HttpResponse("User profile not found.")
        else:
            return HttpResponse("Invalid credentials!")

    return render(request, 'login.html')

# ----------- Role-Based Dashboards -----------

#def admin_dashboard(request):
 #   return render(request, 'admin/admin.html')*/

@login_required
@allowed_roles(['admin'])
def admin_dashboard(request):
    return render(
        request,
        'admin/admin.html'
    )

#def manager_dashboard(request):
 #   return render(request, 'manager/manager.html')
@login_required
@allowed_roles(['teacher'])
def teacher_dashboard(request):
    return render(
        request,
        'teacher/teacher.html'
    )

#def staff_dashboard(request):
 #   return render(request, 'staff/staff.html')
@login_required
@allowed_roles(['student'])
def student_dashboard(request):
    return render(
        request,
        'student/student.html'
    )



# main/views.py



@login_required
@allowed_roles(['admin'])
def makerole(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email    = request.POST.get('email')
        phone    = request.POST.get('phone')
        password = request.POST.get('password')
        role     = request.POST.get('role')

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists!")

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Si el rol es administrador
        if role == 'admin':
            user.is_staff = True
            user.is_superuser = True
            user.save()
        
        # Create profile with role
        UserProfile.objects.create(
            user=user,
            role=role,
            phone=phone,
            signup_time=timezone.now(),
            created_by=request.user  # logged-in admin
        )

        return HttpResponse(f"User '{username}' with role '{role}' created successfully!")

    return render(request, 'admin/makerole.html')

