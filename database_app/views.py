from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.http import QueryDict

def build_url_with_get(*args, **kwargs):
	params = kwargs.pop('params', {})
	url = reverse(*args, **kwargs)
	
	if not params:
		return url

	qdict = QueryDict('', mutable=True)
	for key, value in params.items():
		if type(value) is list:
			qdict.setlist(key, value)
		else:
			qdict[key] = value

	return url + '?' + qdict.urlencode()

	
class Db_Login_View(FormView):
	template_name = 'database_app/login.html'
	form_class = AuthenticationForm
	
	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(Db_Login_View, self).form_valid(form)
		
	def get_context_data(self, **kwargs):
		context = super(Db_Login_View, self).get_context_data(**kwargs)
		
		if 'next' in self.request.GET:
			context['next'] = self.request.GET['next']
		
		if 'logout' in self.request.GET:
			if self.request.GET['logout'].lower() == 'success':
				custom_message = 'User successfully logged out. Kindly login again to work with the Database.'
				context['custom_message'] = custom_message
			
		return context
		
	def get_success_url(self):
		next_url = self.request.POST.get('next',None)
		if next_url:
			return next_url
		else:
			return reverse_lazy('database_app:landing')

class Db_Logout_View(RedirectView):
	
	def get(self, request, *args, **kwargs):
		logout(request)
		return super(Db_Logout_View, self).get(request, *args, **kwargs)
		
	def get_redirect_url(self, *args, **kwargs):
		url = build_url_with_get('database_app:db_login', params = {'logout':'success'})
		return url
		
@login_required()
def landing(request):
	return render(request, 'database_app/landing.html')

@login_required()
def details(request):
	return HttpResponse("DETAILS: Building In Progress")

@login_required()
def profile(request):
	return HttpResponse("PROFILE: Building In Progress")

@login_required()
def stat(request):
	return HttpResponse("STAT: Building In Progress")

@login_required()
def search_results(request):
	return HttpResponse("SEARCH_RESULT: Building In Progress")

@login_required()
def edit(request):
	return HttpResponse("EDIT: Building In Progress")