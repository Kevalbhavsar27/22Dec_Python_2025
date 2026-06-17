from django.shortcuts import render
import razorpay
from django.http import JsonResponse,HttpResponse
import requests
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def index(request):
    return render(request,"index.html")


def payment(request):
    amt = int(request.GET['amt'])
    client = razorpay.Client(auth=("rzp_test_SrVF3qKpUUSwRy", "cQWzjjQRmeAPudfjsoRJNX8i"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    return JsonResponse(payment)


def sendsms(request):
    
    phone = request.GET['phone']
    sms = request.GET['sms']

    url = f"https://www.fast2sms.com/dev/bulkV2?authorization=APIKEY&route=q&numbers={phone}&message={sms}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    return HttpResponse(response.text)



def send_email(request):
    
    send_mail(
        subject=request.GET['subject'],
        message=request.GET['content'],
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[request.GET['to']],
        fail_silently=False,
    )

    return HttpResponse("mail send")