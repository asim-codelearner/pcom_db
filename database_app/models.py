from django.db import models
from django.contrib.auth.models import User
	
class Member_User(models.Model):
	member_user = models.OneToOneField(User)
	
	def __str__(self):
		return self.member_user.username
		
class Executive_User(models.Model):
	user = models.OneToOneField(Member_User)
	
	def __str__(self):
		return self.user.member_user.username + '@ executive'
		
class Senior_User(models.Model):
	user = models.OneToOneField(Member_User)
	executive_mentor = models.ForeignKey(
									Executive_User,
									on_delete = models.SET_NULL, #TODO: Change it to force setting Executive_User
									null = True
								)
								
	def __str__(self):
		senior_user_identifier = self.user.member_user.username + '@ senior'
		return senior_user_identifier
								

class Junior_User(models.Model):
	user = models.OneToOneField(Member_User)
	senior_mentor = models.ForeignKey(
									Senior_User,
									on_delete = models.SET_NULL, #TODO: Change it to force setting Senior_user
									null = True
								)
								
	def __str__(self):
		junior_user_identifier = self.user.member_user.username + '@ junior'
		return junior_user_identifier

class Industry(models.Model):
	industry_name = models.CharField(max_length = 20)
	executive_owner = models.ForeignKey(
									Executive_User,
									on_delete = models.SET_NULL, #TODO: Change it to force setting Executive_User
									null = True
								)
								
	def __str__(self):
		return self.industry_name
		
class Company(models.Model):
	company_name = models.CharField(max_length = 25)
	priority = models.CharField(max_length = 1)
	status = models.CharField(max_length = 10)
	owner = models.ForeignKey(
									Member_User,
									on_delete = models.SET_NULL, #TODO: Change it to force setting Executive_User
									null = True
								)
	industry =  models.ForeignKey(
									Industry,
									on_delete = models.SET_NULL, #TODO: Change it to force setting Industry
									null = True
								)
								
	def __str__(self):
		return self.company_name

class Brand(models.Model):
	brand_name = models.CharField(max_length = 25)
	company = models.ForeignKey(
									Company,
									on_delete = models.CASCADE
							)
							
	def __str__(self):
		return self.brand_name
							
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
	
	def __str__(self):
		details_identifier = self.salutation + ' ' + self.first_name +' @ ' + self.company.company_name
		return details_identifier
	
class Logs(models.Model):
	contact = models.ForeignKey(
									Company_Details,
									on_delete = models.CASCADE
							)
	timestamp = models.DateTimeField(auto_now = True)
	logs = models.TextField()
	
	def __str__(self):
		logs_identifier = 'logs@ ' + self.contact.company.company_name + ' ; ' + self.contact.first_name
		return logs_identifier
