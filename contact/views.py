from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .models import AboutModel

def CONTACT(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Jackfruit Project Contact Form Submission"
            message = (
                f"Message from {form.cleaned_data['name']}\n"
                f"Phone: {form.cleaned_data['phone']}\n"
                f"Email: {form.cleaned_data['gmail']}\n\n"
                f"{form.cleaned_data['text']}"
            )
            from_email = 'myprojects.helpservice@gmail.com'
            recipient_list = ['myprojects.helpservice@gmail.com']
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, 'Successfully submitted your data!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def ABOUT(request):
    obj = AboutModel.objects.all()
    return render(request,'about.html',{'obj':obj})