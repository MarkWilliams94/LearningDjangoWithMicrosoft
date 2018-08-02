#Makes an HTTP request and retuns an HTTP response in views.py

#importing packages (?) for use in functions
from django.shortcuts import render
from django.http import HttpResponse 

#Functions listed below

def index(request): #Defines a view named index
    return HttpResponse("Hello, Django!") 
