from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Person
#from .models import CarouselItem
#from .models import User_Profile

"""
class ProfileInline(admin.StackedInline):
    model = User_Profile
    can_delete = False
    verbose_name_plural = 'profile'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

# Register your models here.
admin.site.unregister(User)
"""

admin.site.register(Person)


