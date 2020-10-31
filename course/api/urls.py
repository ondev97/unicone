from django.urls import path
from .import views

#app_name = "course"

urlpatterns = [
    path('list/', views.ListCourseView.as_view(), name="course_list"),
    path('list/<int:pk>/', views.CourseDetailView.as_view(), name="course_detail"),
    path('create/', views.CreateCourseView.as_view(), name="create_course"),
    path('add-module/', views.CreateModuleView.as_view(), name="add_module"),
]