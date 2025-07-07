from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render ,redirect
from django.core.mail import send_mail
from django.conf import settings
from ..my_app.forms import ContactForm

 
def Home(request):
    return render(request, "Home.html")
 

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            return HttpResponse("Yay! you are human.")
        else:
            return HttpResponse("OOPS! Bot suspected.")
          
    else:
        form = ContactForm()
        
    return render(request, 'contacts.html', {'form':form})



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