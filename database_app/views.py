from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.core.urlresolvers import reverse

def db_login(request):
	
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(username = username, password = password)
		
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('database_app:landing'))
			else:
				error_message = 'Please enter correct username and/or password to login'
				context = {
							'error_message':error_message,
				}
				return render(request, 'database_app/login.html', context)
		else:
			print ("Invalid Login Deatils")
			error_message = 'Please enter correct username and/or password to login'
			context = {
						'error_message':error_message,
			}
			return render(request, 'database_app/login.html', context)
	else:
		return render(request, 'database_app/login.html')
	
	
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