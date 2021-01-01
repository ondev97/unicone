from django.contrib import admin
from .models import User,TeacherProfile,StudentProfile,GroupAdminForm,Group
from django.contrib.auth.admin import UserAdmin

#Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','username','date_joined','last_login','is_admin')
    search_fields = ('email','username')
    readonly_fields = ('date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User,AccountAdmin)
admin.site.register(TeacherProfile)
admin.site.register(StudentProfile)

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


