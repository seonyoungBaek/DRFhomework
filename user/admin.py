from django.contrib import admin
from user.models import User
from user.models import UserProfile
# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
