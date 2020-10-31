from pip._vendor.requests import Response
from rest_framework.decorators import api_view

from course.models import Course,Module
from account.models import TeacherProfile
from course.api.serializer import CourseSerializer,CreateCourseSerializer,CreateModuleSerializer,CourseDetailSerializer
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView,RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

class ListCourseView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class CreateCourseView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CreateCourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print("user:-" ,self.request.user)
        teacher = TeacherProfile.objects.get(user=self.request.user.id)
        serializer.save(author=teacher)

class CreateModuleView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CreateModuleSerializer
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     course = Course.objects.get(id = self.request.course.pk)
    #     print(course)
    #     serializer.save(course=course)







