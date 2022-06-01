from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request, 'profiles/home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'profiles/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('mainpage')
            except IntegrityError:
                return render(request, 'profiles/signupuser.html', {'form': UserCreationForm(), 'error': 'User with this name already excist'})
        else:
            return render(request, 'profiles/signupuser.html', {'form': UserCreationForm(), 'error': 'Password did not match'})

def mainpage(request):
    return render(request, 'profiles/mainpage.html')

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'profiles/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'profiles/loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did nor match'})
        else:
            login(request, user)
            return redirect('mainpage')

        
