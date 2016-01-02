from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

class Db_Login_View(FormView):
	template_name = 'database_app/login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('database_app:landing')
	
	def form_valid(self, form):
		login(self.request, form.get_user())
		return super(Db_Login_View, self).form_valid(form)
		
	def get_context_data(self, **kwargs):
		context = super(Db_Login_View, self).get_context_data(**kwargs)
		if 'status' in self.kwargs:
			if self.kwargs['status'].lower() == 'success':
				custom_message = 'User successfully logged out. Kindly login again to work with the Database.'
				context['custom_message'] = custom_message
			
		return context

def db_logout(request):
	logout(request)
	return redirect(reverse('database_app:db_logout_success', args = ['success']))

@login_required(login_url = reverse_lazy('database_app:db_login'))	
def landing(request):
	return render(request, 'database_app/landing.html')

@login_required(login_url = reverse_lazy('database_app:db_login'))
def details(request):
	return HttpResponse("DETAILS: Building In Progress")

@login_required(login_url = reverse_lazy('database_app:db_login'))
def profile(request):
	return HttpResponse("PROFILE: Building In Progress")

@login_required(login_url = reverse_lazy('database_app:db_login'))
def stat(request):
	return HttpResponse("STAT: Building In Progress")

@login_required(login_url = reverse_lazy('database_app:db_login'))
def search_results(request):
	return HttpResponse("SEARCH_RESULT: Building In Progress")

@login_required(login_url = reverse_lazy('database_app:db_login'))
def edit(request):
	return HttpResponse("EDIT: Building In Progress")