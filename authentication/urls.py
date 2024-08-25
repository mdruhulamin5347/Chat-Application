from django.urls import path
from .views import *
urlpatterns = [
    path('login/',LOGINPAGE,name='login'),
    path('logout/',LOGOUTPAGE,name='logout'),
    path('signUp/',SIGNUP,name='signUp'),
    path('change-password',CHANGE, name='change_password'),
    path('reset-password/',PasswordReset, name='password_reset'),
]
