from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Contact_model(models.Model):
    name=models.CharField(max_length=50, null=True,blank=True)
    gmail=models.EmailField(null=True,blank=True)
    phone=models.PositiveIntegerField(null=True, blank=True)
    text=models.TextField(max_length=500, null=True,blank=True)
    def __str__(self):
        return f"{self.name}"
    

class AboutModel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    details = models.TextField(max_length=500, null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    skill = models.TextField(null=True, blank=True)
    hobby = models.TextField(null=True, blank=True)
    image = models.ImageField(default='profile/default.png', null=True, blank=True)

    def __str__(self):
        return self.name

