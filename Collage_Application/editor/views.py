from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Create your views here.
# import os
# import subprocess
# from django.http import FileResponse
from .forms import ContactForm
# from django.conf import settings
# import uuid

def Home(request):   
    return render(request, 'editor/edit.html')

 

 
  
def contact_view(request):   
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # Access form.cleaned_data and form.cleaned_data['attachment']
            uploaded_file = form.cleaned_data.get('attachment')
            if uploaded_file:
                print("File name:", uploaded_file.name)
                print("File size:", uploaded_file.size)
            return HttpResponse('success')
    else:
        form = ContactForm()
    
    return render(request, 'editor/contact_us.html', {'form': form})

def user_form(request):   
    if request.method == 'POST':
        username=request.POST['username']
        useremail=request.POST['email']
        userpassword=request.POST['password']
        print(username,useremail,userpassword)

          # Simple check if user exists
        if User.objects.filter(email=useremail).exists():
            messages.error(request, "Email already registered")
            return redirect("user_form")

        # Save user with hashed password
        user = User(
            name=username, 
            email=useremail,
            password=make_password(userpassword)  # hash password
        )
        user.save()
        messages.success(request, "User registered successfully!")
        return redirect('/')  # or wherever you want
        
    return  render(request,'editor/user_form.html')

    
