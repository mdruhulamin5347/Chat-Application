from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.utils.crypto import get_random_string


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

def CHANGE(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            # Update the session to prevent the user from being logged out
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('home')  # Redirect to the desired page after success
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'authenticate/change.html', {'form': form})


def PasswordReset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:  
            temp_password = get_random_string(8)         
            user.password = make_password(temp_password)
            user.save()
            
            subject = 'Your Temporary Password for Chat Account'
            message = f'Hi {user.username},\n\nYou requested a password reset for your Chat account. Here is your temporary password: {temp_password}\n\nPlease log in with this password and change it immediately.\n\nThank you!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email]
            send_mail(subject, message, email_from, recipient_list)

            messages.success(request, 'A temporary password has been sent to your email. Please check your inbox.')
            return redirect('login')
        else:
            messages.warning(request, 'Invalid email address!')
            return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))
