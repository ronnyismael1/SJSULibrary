from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, librarians_only, admin_only

#### USER REGISTRATION AND LOGIN
@unauthenticated_user
def registerPage(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='student')
            user.groups.add(group)
            
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'access_control/register.html', context)
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'access_control/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
###############################

## Student Access
@login_required(login_url='login')
@allowed_users(['admin', 'librarian', 'student'])
def home(request):
    is_student = request.user.groups.filter(name='student').exists()
    is_librarian = request.user.groups.filter(name='librarian').exists()
    is_admin = request.user.groups.filter(name='admin').exists()
    context = {
        'is_student': is_student,
        'is_librarian': is_librarian,
        'is_admin': is_admin
    }
    return render(request, 'access_control/home.html', context)
@login_required(login_url='login')
@allowed_users(['admin', 'librarian', 'student'])
def books(request):
    return render(request, 'access_control/books.html')

## Librarian Access
@login_required(login_url='login')
@librarians_only
def checkout(request):
    return render(request, 'access_control/checkout.html')
@login_required(login_url='login')
@librarians_only
def addNew(request):
    return render(request, 'access_control/addNew.html')

## Admin Access
@login_required(login_url='login')
@admin_only
def reports(request):
    return render(request, 'access_control/reports.html')
@login_required(login_url='login')
@admin_only
def addLibrarian(request):
    if request.method == 'POST':
        # Check which form is submitted
        if 'student_id' in request.POST:
            user_id = request.POST.get('student_id')
            from_group = Group.objects.get(name='student')
            to_group = Group.objects.get(name='librarian')
        elif 'librarian_id' in request.POST:
            user_id = request.POST.get('librarian_id')
            from_group = Group.objects.get(name='librarian')
            to_group = Group.objects.get(name='student')

        user = User.objects.get(id=user_id)
        user.groups.remove(from_group)
        user.groups.add(to_group)
        messages.success(request, f'{user.username} has been changed to {to_group.name}.')
        return redirect('addLibrarian')
    else:
        students = User.objects.filter(groups__name='student')
        librarians = User.objects.filter(groups__name='librarian')
        return render(request, 'access_control/addLibrarian.html', {'students': students, 'librarians': librarians})

