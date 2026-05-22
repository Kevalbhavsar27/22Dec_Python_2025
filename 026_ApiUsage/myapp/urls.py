from django.urls import path
from myapp.views import *

urlpatterns = [
    path("",index,name="index"),
    path("payment",payment,name="payment"),
    path("sendsms",sendsms,name="sendsms"),
    path("sendemail",send_email,name="sendemail")
]