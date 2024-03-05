from django.shortcuts import render,redirect
from .forms import contact_form
from django.contrib import messages
# Create your views here.


def CONTACT(request):
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(request,'successfully submited your data!')
            return redirect('contact')
    else:
        form=contact_form()
    return render(request,'contact.html',{'form':form})

def ABOUT(request):
    return render(request,'about.html')