from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserCreateForm
# Create your views here.


def LOGINPAGE(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'succesfully logined')
                return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request,'authenticate/login.html', {'form':form})


def LOGOUTPAGE(request):
    logout(request)
    messages.success(request, 'successfully logout the page')
    return redirect('home')


def SIGNUP(request):
    if request.method=='POST':
        form=UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreateForm()
    return render(request, 'authenticate/signup.html', {'form':form})
