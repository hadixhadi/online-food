from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User
# Register your models here.
class customUserAdmin(UserAdmin):
    list_display=('first_name','last_name',
                  'username',
                  'email','phone_number',
                  'role',)
    
    ordering=('-date_joined',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()


admin.site.register(User,customUserAdmin)