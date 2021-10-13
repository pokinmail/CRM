from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#from .models import User
from .models import Team

admin.site.register(Team)

'''
# Define an inline admin descriptor for Staff model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
'''