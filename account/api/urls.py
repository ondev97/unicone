from django.urls import path,include
from account.api.views import createuser
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',createuser.as_view(),name='register'),




]
