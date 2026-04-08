from django.urls import path
from myapp.views import *


urlpatterns = [
    path("",login_page,name="loginpage"),
    path("reg",reg_page,name="reg"),
    path("home",home,name="home"),
    path("logout",user_logout,name="logout")

]