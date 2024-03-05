from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact_model(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50, null=True,blank=True)
    gmail=models.EmailField(null=True,blank=True)
    phone=models.PositiveIntegerField(null=True)
    text=models.TextField(null=True,blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.name}"