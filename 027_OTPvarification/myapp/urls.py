from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("reg",reg,name="reg"),
    path("otp",otp,name="otp"),
    path("forgot",forgot,name="forgot"),
    path("reset",reset,name="reset")
]