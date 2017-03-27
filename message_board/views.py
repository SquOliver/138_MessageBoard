from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello World! This is the message board index.");

def lol(request):
	return HttpResponse("Regular Expression");
