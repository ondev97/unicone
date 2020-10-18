from django.urls import path
from account.api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('teacher/', views.registration_view, name='register'),
    path('student/', views.sturegistration_view, name='sturegister'),
    path('login/', obtain_auth_token, name='login'),



]
