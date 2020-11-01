from django.urls import path
from .import views

#app_name = "course"

urlpatterns = [
    path('list/', views.ListCourseView.as_view(), name="course_list"),
    path('view/<int:pk>/', views.ViewCourse, name="view_course"),
    path('create/', views.CreateCourseView.as_view(), name="create_course"),
    path('update/<int:pk>/', views.UpdateCourse.as_view(), name="update_course"),
    path('module/<int:pk>/', views.AddModule, name="add_module"),
    path('modulelist/', views.ModuleList, name="modules"),

]