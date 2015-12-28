from django.db import models
from django.contrib.auth.models import User

class Executive_User(models.Model):
	user = models.OneToOneField(User)
	
class Member_User(models.Model):
	user = models.OneToOneField(User)
	
class Senior_User(models.Model):
	user = models.OneToOneField(Member_User)
	executive_mentor = models.ForeignKey(
									Executive_User,
									on_delete = models.SET_NULL #TODO: Change it to force setting Executive_User
								)

class Junior_User(models.Model):
	user = models.OneToOneField(Member_User)
	senior_mentor = models.ForeignKey(
									Senior_User,
									on_delete = models.SET_NULL #TODO: Change it to force setting Senior_user
								)

class Industry(models.Model):
	industry_name = models.CharField(max_length = 20)
	executive_owner = models.ForeignKey(
									Executive_User,
									on_delete = models.SET_NULL #TODO: Change it to force setting Executive_User
								)
								
class Company(models.Model):
	company_name = models.CharField(max_length = 25)
	priority = models.CharField(max_length = 1)
	status = modles.CharField(max_length = 10)
	owner = models.ForeignKey(
									Member_User,
									on_delete = models.SET_NULL #TODO: Change it to force setting Executive_User
								)
	industry =  models.ForeignKey(
									Industry,
									on_delete = models.SET_NULL #TODO: Change it to force setting Industry
								)

class Brand(models.Model):
	brand_name = models.CharField(max_length = 25)
	company = models.ForeignKey(
									Company,
									on_delete = models.CASCADE
							)
							
class Company_Details(models.Model):
	company = models.ForeignKey(
									Company,
									on_delete = models.CASCADE
							)
	city = models.CharField(max_length = 25)
	salutation = models.CharField(max_length = 3)
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 20)
	e_mail = models.EmailField()
	board_number = models.CharField(max_length = 12)#TODO: Change it appropriately
	mobile_number = models.CharField(max_length = 12)
	address = models.TextField()
	is_correct_contact = models.BooleanField()
	
class Logs(models.Model):
	contact = models.ForeignKey(
									Company_Details,
									on_delete = models.CASCADE
							)
	timestamp = models.DateTimeField(auto_now = True, auto_now_add = True)
	logs = models.TextField()
	