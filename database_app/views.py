from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext

def db_login(request):
	context = RequestContext(request)
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(username = username, password = password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/landing/')
			else:
				return HttpResponse("Account Disabled")
		else:
			print ("Invalid Login Deatils")
			return HttpResponse("Invalid Login details supplied")
	else:
		return render_to_response('/', {}, context)
	
	
def landing(request):
	return HttpResponse("LANDING: Building In Progress")
	
def details(request):
	return HttpResponse("DETAILS: Building In Progress")

def profile(request):
	return HttpResponse("PROFILE: Building In Progress")
	
def stat(request):
	return HttpResponse("STAT: Building In Progress")
	
def search_results(request):
	return HttpResponse("SEARCH_RESULT: Building In Progress")
	
def edit(request):
	return HttpResponse("EDIT: Building In Progress")