from django.contrib import admin

from .models import UserProfile, UserPersona, UserInterest

# models that can be modified using the admin interface
admin.site.register(UserProfile)
admin.site.register(UserPersona)
admin.site.register(UserInterest)
