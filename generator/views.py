from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	return render(request,'generator/home.html',{'password':'abcd123'})

def password(request):
	thepassword = ''
	characters = list("abcdefghijklmnopqrstuvwxyz")
	numbers = list("01234567890")
	uppercase = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	special = list("!@#$%^&*()?")
	length = int(request.GET.get('Length'))
	if request.GET.get('uppercase'):
		characters.extend(uppercase)
	if request.GET.get('special'):
		characters.extend(special)
	if request.GET.get('numbers'):
		characters.extend(numbers)
	for x in range(length):
		thepassword += random.choice(characters)
	return render(request,'generator/password.html',{'password':thepassword}) 

def about(request):
	return render(request,'generator/about.html')