from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def db_login(request, *args, **kwargs):
	
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		
		if form.is_valid():
		
			login(request, form.get_user())
			return HttpResponseRedirect(reverse('database_app:landing'))
	
	else:
		form = AuthenticationForm()
	
	context = {
				'login_form':form,
			}
	print(kwargs)
	if 'status' in kwargs:
		if kwargs['status'].lower() == 'success':
			custom_message = 'User successfully logged out. Kindly login again to work with the Database.'
			context['custom_message'] = custom_message
	print(context)
	return render(request, 'database_app/login.html', context)

def db_logout(request):
	logout(request)
	return redirect('/logout/success')

@login_required(login_url = '/')	
def landing(request):
	return render(request, 'database_app/landing.html')

@login_required(login_url = '/')	
def details(request):
	return HttpResponse("DETAILS: Building In Progress")

@login_required(login_url = '/')	
def profile(request):
	return HttpResponse("PROFILE: Building In Progress")

@login_required(login_url = '/')	
def stat(request):
	return HttpResponse("STAT: Building In Progress")

@login_required(login_url = '/')	
def search_results(request):
	return HttpResponse("SEARCH_RESULT: Building In Progress")

@login_required(login_url = '/')	
def edit(request):
	return HttpResponse("EDIT: Building In Progress")