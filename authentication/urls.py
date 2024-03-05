from django.urls import path
from .views import *
urlpatterns = [
    path('login/',LOGINPAGE,name='login'),
    path('logout/',LOGOUTPAGE,name='logout'),
    path('signUp/',SIGNUP,name='signUp'),
]
