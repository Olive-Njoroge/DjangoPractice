from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("tech with Olive!")

def v1(response):
    return HttpResponse("View 1")

def hello_world(response):
    return HttpResponse("Hello World!")
