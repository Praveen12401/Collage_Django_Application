from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render ,redirect
from django.core.mail import send_mail
from django.conf import settings
 


 
def Home(request):
    return render(request, "Home.html")
 

def about(request):
    return render(request, "about.html")

def contacts(request):   
    return render(request, 'contacts.html')

def login(request):   
    return render(request, 'login.html')



def send_mail_page(request):
    context = {}

    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = f'Error sending email: {e}'
        else:
            context['result'] = 'All fields are required'
    
    return render(request, "MailApp.html", context) 


import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

CLERK_SECRET_KEY = "your-clerk-secret-key"

@csrf_exempt
def clerk_callback(request):
    session_token = request.headers.get("Authorization")
    if not session_token:
        return JsonResponse({"error": "Missing token"}, status=401)

    headers = {
        "Authorization": session_token,
        "Content-Type": "application/json",
    }

    response = requests.get(
        "https://api.clerk.com/v1/sessions",
        headers=headers
    )

    if response.status_code == 200:
        session_data = response.json()
        # You can now map Clerk user to your Django user model
        return JsonResponse(session_data)
    else:
        return JsonResponse({"error": "Invalid session"}, status=403)
    
 
