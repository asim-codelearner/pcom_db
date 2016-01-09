from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.template import RequestContext
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.views.generic.base import RedirectView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import QueryDict
from django.contrib.auth.views import password_change
from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.forms import models as model_forms
#from django.contrib.auth import User

def build_url_with_get(*args, **kwargs):
	params = kwargs.pop('params', {})
	url = reverse_lazy(*args, **kwargs)
	print(url)
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

			
class Db_Logout_View(LoginRequiredMixin, RedirectView):
	login_url = reverse_lazy('database_app:db_login')
	
	def get(self, request, *args, **kwargs):
		logout(request)
		return super(Db_Logout_View, self).get(request, *args, **kwargs)
		
	def get_redirect_url(self, *args, **kwargs):
		url = build_url_with_get('database_app:db_login', params = {'logout':'success'})
		return url

		
class Password_Change_View(LoginRequiredMixin, FormView):
	login_url = reverse_lazy('database_app:db_login')
	
	template_name = 'database_app/password_change_form.html'
	form_class = PasswordChangeForm
	
	def get_form_kwargs(self):
		kwargs = super(Password_Change_View, self).get_form_kwargs()
		user = self.request.user
		kwargs['user'] = user
		
		return kwargs
	
	def form_valid(self, form):
		print('form_valid called')
		form.save()
		# Updating the password logs out all other sessions for the user
		# except the current one if
		# django.contrib.auth.middleware.SessionAuthenticationMiddleware
		# is enabled.
		update_session_auth_hash(self.request, form.user)
		return super(Password_Change_View, self).form_valid(form)
		
	def get_context_data(self, **kwargs):
		context = super(Password_Change_View, self).get_context_data(**kwargs)
		
		context['menu_items'] = [{'link_url':reverse_lazy('database_app:db_logout'), 'display_label':'Log out'}]
		print(context)
		return context
		
	def get_success_url(self):
		next_url = build_url_with_get('database_app:landing', params = {'password_change':'success'})
		return next_url
	
	
#@method_decorator(login_required, name = 'dispatch')
class Db_Landing_View(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('database_app:db_login')
	
	template_name = 'database_app/landing.html'
	paginate_by = 10
	ordering = 'company_name'
	
	logs_model = models.Logs
	logs_field = ['logs']
	
	def get_queryset(self):
		self.queryset = models.Company.objects.filter(owner_id = self.request.user.id)
		queryset = super(Db_Landing_View, self).get_queryset()
		return queryset
		
	def get_form_class(self):
		return model_forms.modelform_factory(self.logs_model, fields=self.logs_field)
		
	def get_form(self):
		form_class = self.get_form_class()
		return form_class(**self.get_form_kwargs())
	
	def get_form_kwargs(self):
		kwargs = {}
		
		if self.request.method in ('POST'):
			kwargs.update({
				'data': self.request.POST,
			})
		return kwargs
	
	def form_valid(self, form):
		logs_text = form.cleaned_data['logs']
		contact_id = self.request.POST.get('company_details_id')
		contact = models.Company_Details.objects.get(pk=contact_id)
		
		logs = models.Logs(contact = contact, logs = logs_text)
		logs.save()
		
		return HttpResponseRedirect(self.get_success_url())#TODO: Success URL
	
	def get_success_url(self):
		return self.request.get_full_path()
		
	def form_invalid(self, form):
		"""
		If the form is invalid, re-render the context data with the
		data-filled form and errors.
		"""
		return self.render_to_response(self.get_context_data())
		
	def post(self, request, *args, **kwargs):#TODO: Change it according to this view
		"""
		Handles POST requests, instantiating a form instance with the passed
		POST variables and then checked for validity.
		"""
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
		
	def get_menu_items(self):	
		menu_items = [
						{'link_url':reverse_lazy('database_app:password_change'), 'display_label':'Change password'},
						{'link_url':reverse_lazy('database_app:db_logout'), 'display_label':'Log out'},
		]
		
		return menu_items
			
	def get_context_data(self, **kwargs):
		context= super(Db_Landing_View, self).get_context_data(**kwargs)
		context['users_name'] = self.request.user.get_full_name()
		context['menu_items'] = self.get_menu_items()
		context['logs_form'] = self.get_form()
		
		if 'password_change' in self.request.GET:
			if self.request.GET['password_change'].lower() == 'success':
				custom_message = 'Password changed successfully.'
				context['custom_message'] = custom_message
				
		return context
			
# @login_required()
# def landing(request):
	# context = {}
	
	# if 'password_change' in request.GET:
		# if request.GET['password_change'].lower() == 'success':
				# custom_message = 'Password changed successfully.'
				# context['custom_message'] = custom_message
	# return render(request, 'database_app/landing.html', context)

# class Db_Details_View(LoginRequiredMixin, DetailView):
	# login_url = reverse_lazy('database_app:db_login')
	
	
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