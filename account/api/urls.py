from django.urls import path,include
from account.api.views import createuser, TeacherProfileView, UpdateTeacherProfileView, LogoutView, TestLoginView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',createuser.as_view(),name='register'),
    path('profile/<int:pk>/',TeacherProfileView,name='view_profile'),
    path('updateteacher/<int:pk>/',UpdateTeacherProfileView,name='update_teacher'),
    path('logout/',LogoutView.as_view(),name='update_teacher'),
    path('testlogin/',TestLoginView,name='test_login'),

]
