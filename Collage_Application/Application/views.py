from django.http import HttpResponse, HttpResponseRedirect

 
from django.shortcuts import render, redirect

def Home(request):
    return render(request, "Home.html")
 

def about(request):
    return render(request, "about.html")