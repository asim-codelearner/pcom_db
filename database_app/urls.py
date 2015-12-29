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
from . import views

urlpatterns = [
	url(r'^$', views.db_login, name = 'db_login'),
	url(r'^landing/$', views.landing, name = 'landing'),
	url(r'^details/$', views.details, name = 'details'),
	url(r'^profile/$', views.profile, name = 'profile'),
	url(r'^stat/$', views.stat, name = 'stat'),
	url(r'^search_results/$', views.landing, name = 'search_results'),
	url(r'^edit/$', views.edit, name = 'edit'),
]