from django.db import models
from django.contrib.auth.models import User


class To_do_list(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_list', null=True,blank=True)
    work_time = models.TimeField(null=True,blank=True)
    work_name = models.CharField(max_length=100, null=True,blank=True)
    done_bol = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.username} - {self.work_time} - {self.work_name}"




class Success_day(models.Model):
    username=models.ForeignKey(User, on_delete=models.CASCADE, related_name='success', null=True,blank=True)
    done_count = models.IntegerField(default=0)
    percentage_score=models.FloatField(null=True)

  