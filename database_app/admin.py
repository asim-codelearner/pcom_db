from django.contrib import admin, auth
from .models import Executive_User, Senior_User, Junior_User, Company, Industry, Brand, Company_Details, Logs
from django.conf import settings
#from django.contrib.auth.models import User

admin.site.register(Executive_User)
admin.site.register(Senior_User)
admin.site.register(Junior_User)
admin.site.register(Industry)
admin.site.register(Company)
admin.site.register(Brand)
admin.site.register(Company_Details)
admin.site.register(Logs)

