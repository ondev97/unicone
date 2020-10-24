from django.contrib import admin
from .models import User,TeacherProfile,StudentProfile
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


