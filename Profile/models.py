from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Profile_update(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    address = models.CharField(max_length=100, null=True,blank=True)
    image = models.ImageField(default='profile/default.png', upload_to='profile/')
    def __str__(self):
        return self.user.username
    






class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE, null=True,blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender}'
    

class NotificationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Notification for {self.user.username} - {self.message[:20]}"


