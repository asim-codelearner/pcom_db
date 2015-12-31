from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.core.urlresolvers import reverse
#from .forms import Login_Form
from django.contrib.auth.forms import AuthenticationForm

def db_login(request):
	
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
	return render(request, 'database_app/login.html', context)
		
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