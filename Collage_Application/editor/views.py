from django.shortcuts import render ,redirect
from django.http import HttpResponse

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
    
    return render(request, 'editor/contact.html', {'form': form})

    
