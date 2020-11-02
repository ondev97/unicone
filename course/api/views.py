from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from course.models import Course,Module
from account.models import TeacherProfile,StudentProfile
from course.api.serializer import (CourseSerializer,
                                   CourseDetailSerializer,
                                   CourseCreateSerializer,
                                   ModuleSerializer,
                                   CourseEnrollSerializer)
from rest_framework.generics import( ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView,
                                     RetrieveUpdateAPIView,
                                     UpdateAPIView,
                                     ListCreateAPIView)
from rest_framework.permissions import IsAuthenticated

# Views for Unauthenticated Users

# List all Courses

class ListCourse(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# course info

class CourseRetrieve(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


# views for authenticated users

# creating courses and modules

class CreateCourseView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print("user:-" ,self.request.user)
        teacher = TeacherProfile.objects.get(user=self.request.user.id)
        serializer.save(author=teacher)

# updating courses and modules within the course
class UpdateCourse(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_classes = [IsAuthenticated]

# creating a separate module


@permission_classes((IsAuthenticated))
@api_view(['POST'])
def CreateModule(request,pk):
    course = Course.objects.get(id=pk)
    print(course)
    serializer = ModuleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(course=course)
    return Response(serializer.data)


# views for Students

# course Enroll

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EnrollCourse(request,pk):
    course = Course.objects.get(id=pk)
    print("course",course)
    student = StudentProfile.objects.get(user=request.user)
    print("student",student)
    serializer = CourseEnrollSerializer(data=request.data,many=True)
    print("loading the serializer...")
    if serializer.is_valid():
        print("serializer is valid")
        serializer.save(course=course)
        print("course saved")
        serializer.save(student=student)
        print("student saved")
    else:
        print("Serializer not valid",serializer.errors)
    return Response(serializer.data)


# class UpdateCourse(RetrieveUpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseDetailSerializer
#     permission_classes = [IsAuthenticated]















# #List courses for unauthenticated users
# class ListCourseView(ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#
# #creating courses and modules
# class CreateCourseView(CreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         print("user:-" ,self.request.user)
#         teacher = TeacherProfile.objects.get(user=self.request.user.id)
#         serializer.save(author=teacher)
#
#updating courses and modules
# class UpdateCourse(RetrieveUpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#
# @api_view(['POST'])
# def AddModule(request,pk):
#     course = Course.objects.get(id=pk)
#     print(course)
#     serializer = ModuleSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(course=course)
#     return Response(serializer.data)
#
# @api_view(['GET',])
# def ModuleList(request):
#     courses = Course.objects.all()
#     serializer = CourseSerializer(courses,many=True)
#     return Response(serializer.data)
#
#
#
