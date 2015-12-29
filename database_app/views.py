from django.http import HttpResponse
from django.shortcuts import render

def db_login(request):
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