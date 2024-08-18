from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile_update,Message
from .forms import profile_update_form
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone
from notifications.signals import notify
from django.urls import reverse
from .forms import ProfileUpdateForm


@login_required
def profileUpdate(request):
    user = request.user  

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile_view') 
    else:
        form = ProfileUpdateForm(instance=user)
    
    return render(request, 'profile/profile_update.html', {'form': form})




def profileUpdateImage(request):
    try:
        instance=Profile_update.objects.get(user=request.user)
    except Profile_update.DoesNotExist :
        instance=None
    if request.method=="POST":
        if instance:
            form=profile_update_form(request.POST, request.FILES, instance=instance)
        else:
            form=profile_update_form(request.POST, request.FILES)

        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=request.user
            obj.save()
            messages.success(request,'successfully updated your profile')
            return redirect('profile_view')
    else:
        form=profile_update_form(instance=instance)
    return render(request, 'profile/update_profile_image.html',{'form':form})



@login_required
def profileView(request):
    user = Profile_update.objects.get_or_create(user=request.user)[0]
    return render(request, 'profile/profile.html', {'user': user,})




@login_required

def user_chat_list(request):
    users = User.objects.exclude(pk=request.user.pk).select_related('profile_update')
    user_chat_list = []

    for user in users:
        latest_message_sent = Message.objects.filter(sender=request.user, recipient=user).last()
        latest_message_received = Message.objects.filter(sender=user, recipient=request.user).last()


        latest_message = latest_message_sent if latest_message_sent and (
            not latest_message_received or latest_message_sent.timestamp > latest_message_received.timestamp
        ) else latest_message_received

        profile = user.profile_update if hasattr(user, 'profile_update') else None

        user_chat_list.append({'user': user, 'latest_message': latest_message, 'profile': profile})

    user_chat_list.sort(key=lambda x: x['latest_message'].timestamp if x['latest_message'] else datetime.min.replace(tzinfo=timezone.utc), reverse=True)
    return render(request, 'profile/user_list.html', {'user_chat_list': user_chat_list})

def send_message(request, recipient_id):
    recipient = User.objects.get(pk=recipient_id)
    
    # Mark all notifications related to the recipient as read
    NotificationModel.objects.filter(user=request.user, is_read=False).update(is_read=True)
    
    if request.method == 'POST':
        text = request.POST.get('text')
        message = Message.objects.create(sender=request.user, recipient=recipient, content=text)
        message.save()
        if message:
            notify_message = message
            notify_message_content = notify_message.content[:40]
            NotificationModel.objects.create(
            user=recipient,
            message=f'You have received a new message from {request.user.username}: {notify_message_content}... <a href="{reverse("send_message", args=[request.user.id])}">Details</a>'
            )

        if request.user != recipient:
            notification_message = f'sent you a message <a style="color:black" href="{reverse("send_message", args=[request.user.id])}">Details</a>'
            notify.send(request.user, recipient=recipient, verb=notification_message, description=text, target=message)
        
        return redirect('send_message', recipient_id)
    
    sent_messages = Message.objects.filter(sender=request.user, recipient=recipient)
    received_messages = Message.objects.filter(sender=recipient, recipient=request.user)
    all_messages = sent_messages | received_messages
    all_messages = all_messages.order_by('-timestamp')
    
    user = Profile_update.objects.get_or_create(user=recipient)[0]
    request_user = Profile_update.objects.get_or_create(user=request.user)[0]   

    

    return render(request, 'profile/send_message.html', {'recipient': recipient, 'messages': all_messages, 'user': user, 'request_user': request_user})




def Notification(request):
    return render(request, 'profile/notification.html')

from .models import NotificationModel

def notification_list(request):
    notifications = NotificationModel.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'notification_list.html', {'notifications': notifications})

# def mark_as_read(request, notification_id):
#     notification = get_object_or_404(NotificationModel, id=notification_id, user=request.user)
#     notification.is_read = True
#     notification.save()
#     return redirect('notification_list')




