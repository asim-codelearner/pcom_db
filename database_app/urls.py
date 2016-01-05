"""database_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
#from django.contrib.auth.views import password_change, logout, password_change_done
#from django.core.urlresolvers import reverse, reverse_lazy
from .views import Db_Login_View, Db_Logout_View, Password_Change_View, Db_Landing_View
from . import views

	
urlpatterns = [
	url(r'^$', Db_Login_View.as_view(), name = 'db_login'),
	#url(r'^landing/$', views.landing, name = 'landing'),
	url(r'^landing/$', Db_Landing_View.as_view(), name = 'landing'),
	#url(r'^details/$', views.details, name = 'details'),
	#url(r'^profile/$', views.profile, name = 'profile'),
	#url(r'^stat/$', views.stat, name = 'stat'),
	#url(r'^search_results/$', views.landing, name = 'search_results'),
	#url(r'^edit/$', views.edit, name = 'edit'),
	url(r'^logout/$', Db_Logout_View.as_view(), name = 'db_logout'),
	#url(r'^logout/$', logout, name = 'db_logout'),
	url(r'^password_change/$', Password_Change_View.as_view(), name = 'password_change'),
	#url(r'^password_change/$', password_change, {'template_name':'database_app/password_change_form.html', 'post_change_redirect':'/landing/?password_change=success'},name = 'change_password'),
	#url(r'^password_change/done/$', password_change_done, name='password_change_done'),
]