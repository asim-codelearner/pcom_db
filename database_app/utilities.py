class Utilities:
	def get_user_profile(self, user):
		try:
			exec_user = user.executive_user
		except ObjectDoesNotExist:
			pass
		else:
			return exec_user
			
		try:
			senior_user = user.senior_user
		except ObjectDoesNotExist:
			pass
		else:
			return senior_user
			
		try:
			junior_user = user.junior_user
		except ObjectDoesNotExist:
			pass
		else:
			return junior_user