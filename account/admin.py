from django.contrib import admin
from .models import User, TeacherProfile, StudentProfile, GroupAdminForm, Group, StaffProxyModel
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.models import Token

#Register your models here.

class FilterTokenAdmin(admin.ModelAdmin):
    search_fields = ['user__email','user__username']



class AccountAdmin(UserAdmin):
    list_display = ('email','username','date_joined','last_login','is_admin')
    search_fields = ('email','username')
    readonly_fields = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class StudentAdmin(admin.ModelAdmin):
    model = StudentProfile
    search_fields = ['user__email','user__username']


    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class StaffProxyModelAdmin(UserAdmin):
    search_fields = ['email', 'username']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User,AccountAdmin)
admin.site.register(TeacherProfile)
#admin.site.register(StudentProfile,StudentAdmin)
admin.site.register(StaffProxyModel,StaffProxyModelAdmin)

# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
admin.site.register(Token,FilterTokenAdmin)


