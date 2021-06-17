from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
  
def hello(request):  
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")

def index(request):  
   template = loader.get_template('index.html') # getting our template  
   return HttpResponse(template.render())

def next1(request):
   template = loader.get_template('next1.html') # getting our template  
   return HttpResponse(template.render())

def next2(request):
   template = loader.get_template('next2.html') # getting our template  
   return HttpResponse(template.render())

def main(request):
   template = loader.get_template('main.html') # getting our template  
   return HttpResponse(template.render())   
