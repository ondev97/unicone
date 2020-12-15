from django.urls import path,include
from account.api.views import ( createuser,
                                TeacherProfileView,
                                UpdateTeacherProfileView,
                                LogoutView,
                                TestLoginView,
                                UpdateUser,
                                StudentProfileView,
                                UpdateStudentProfileView)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',createuser.as_view(),name='register'),
    path('profile/<int:pk>/',TeacherProfileView,name='view_profile'),
    path('updateteacher/<int:pk>/',UpdateTeacherProfileView,name='update_teacher'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('testlogin/',TestLoginView,name='test_login'),
    path('updateuser/<int:pk>/',UpdateUser.as_view(),name='update_user'),
    path('stuprofile/<int:pk>/',StudentProfileView,name='view_stuprofile'),
    path('updatestudent/<int:pk>/',UpdateStudentProfileView,name='update_student'),

]
