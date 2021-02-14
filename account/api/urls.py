from django.urls import path,include
from django.contrib.auth import views as auth_views
from account.api.views import ( createuser,
                                TeacherProfileView,
                                UpdateTeacherProfileView,
                                LogoutView,
                                TestLoginView,
                                UpdateUser,
                                StudentProfileView,
                                UpdateStudentProfileView,
                                Allteachers,ContactForm,
                                GetStudents)
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
    path('testlogin/',TestLoginView,name='test_login'),
    path('getstudents/<int:id>/',GetStudents,name='get_students'),

    #password reset views

    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


    #index page views

    path('teachers/',Allteachers,name="all_teachers"),

    # contact form

    path('contact/',ContactForm,name="contact")
]
