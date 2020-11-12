from django.contrib import admin
from .models import Course, Module, Enrollment, Coupon

# Register your models here.
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Enrollment)
admin.site.register(Coupon)