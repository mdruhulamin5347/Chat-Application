from django.urls import path
from .views import *

urlpatterns = [
    path('contact/',CONTACT,name='contact'),
    path('about/',ABOUT,name='about'),
]
