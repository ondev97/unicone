from django.urls import path
from .import views

#app_name = "course"

urlpatterns = [
    path('list/',views.ListCourse.as_view(),name='list_course'),
    path('list/<int:pk>',views.CourseRetrieve.as_view(),name='course_info'),
    path('createcourse/',views.CreateCourseView.as_view(),name='create_course'),
    path('updatecourse/<int:pk>/',views.UpdateCourse.as_view(),name='update_course'),
    path('createmodule/<int:pk>/',views.CreateModule,name='create_module'),

]