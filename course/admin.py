from django.contrib import admin
from .models import Course, Module, Enrollment, Coupon, Subject

# Register your models here.
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Enrollment)
admin.site.register(Coupon)
admin.site.register(Subject)