from django.urls import path
from .import views

#app_name = "course"

urlpatterns = [
    path('list/',views.ListCourse.as_view(),name='list_course'),
    path('list/<int:pk>/',views.CourseRetrieve.as_view(),name='course_info'),
    path('createcourse/',views.CreateCourseView.as_view(),name='create_course'),
    path('updatecourse/<int:pk>/',views.UpdateCourse.as_view(),name='update_course'),
    path('createmodule/<int:pk>/',views.CreateModule,name='create_module'),
    path('enrollcourse/<int:pk>/',views.EnrollCourse,name='enroll_course'),
    path('coupon/<int:count>/<int:pk>/',views.CouponGenerator,name='coupon_generator'),
    path('availablecoupon/<int:pk>/',views.AvailableCoupon,name='available_coupon'),
    path('issuecoupon/',views.IssueCoupon,name='issue_coupon'),
    path('mycourses/',views.MyCourses,name='mycourses'),
    path('mycoursesteacher/',views.TeacherCourses,name='mycoursesteacher'),
    path('viewcourse/<int:pk>/',views.ViewEnrolledCourse.as_view(),name='view_course'),
    path('deletecourse/<int:pk>/',views.DeleteCourse,name='delete_course'),
    path('deletemodule/<int:pk>/',views.DeleteModule,name='delete_module'),
    path('updatemodule/<int:pk>/',views.UpdateModule,name='update_module'),

]