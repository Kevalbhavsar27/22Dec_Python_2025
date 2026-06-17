from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
from django.conf import settings
import random
def index(request):
    if request.method=='POST':
        data = request.POST
        uname = data.get("username")
        password = data.get("password")

        u = authenticate(username=uname,password=password)
        print(u)
        if u is not None:
            otp = random.randint(100,999)
            request.session['otp']=otp
            send_mail(
            subject='OTP varification',
            message=f"Your otp is {otp}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[u.email],
            fail_silently=False,
            )
            return render(request,"otp.html")
        else:
            return render(request,"index.html",{"msg":"Invalid credentials"})
    return render(request,"index.html")

def reg(request):
    if request.method=='POST':
        data = request.POST
        fname = data.get("firstname")
        lname = data.get("lastname")
        uname = data.get("username")
        password = data.get("password")
        email = data.get("email")

        User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=password,email=email)
        return render(request,"reg.html",{"msg":"Registration successfully"})
    return render(request,"reg.html")


def otp(request):
    otp = request.POST['otp']
    r_otp = request.session.get('otp')
    if int(otp)==int(r_otp):
        return render(request,"home.html")
    else:
        return render(request,"otp.html",{"err":"Invalid OTP"})
    
def forgot(request):
    if request.method=='POST':
        email = request.POST['email']
        try : 
           
            u = User.objects.get(email=email)
            link = f"http://127.0.0.1:8000/reset?id={u.id}"
            send_mail(
            subject='Reset password',
            message=f"click here to reset password {link}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[u.email],
            fail_silently=False,
            )
        except Exception as e:
             return render(request,"forgot.html",{"err":"somethin went wrong"})

    return render(request,"forgot.html")

def reset(request):
    id  =request.GET['id']
    if request.method=='POST':
        password = request.POST['password']
        user = User.objects.get(id=id)
        user.set_password(password)
        user.save()
    return render(request,"resetpass.html")