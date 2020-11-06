from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from course.models import Course,Module,Enrollment
from account.models import TeacherProfile,StudentProfile
from course.api.serializer import (CourseSerializer,
                                   CourseDetailSerializer,
                                   CourseCreateSerializer,
                                   ModuleSerializer,
                                   CourseEnrollSerializer,
                                   EnrolledCourseSerializer,
                                   MycoursesSerializer)
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
    module = Module(course=course)
    print("important", module.course)
    if request.method == "POST":
        serializer = ModuleSerializer(module, data=request.data)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response(serializer.errors)


# views for Students

# course Enroll

@permission_classes([IsAuthenticated])
@api_view(['POST'])
def EnrollCourse(request,pk):
    course = Course.objects.get(id=pk)
    student = StudentProfile.objects.get(user=request.user)
    enroll = Enrollment(course=course,student=student)
    if request.method == "POST":
        e = Enrollment.objects.filter(course=course, student=student).first()
        if not e:
            serializer = CourseEnrollSerializer(enroll, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response("You have already enrolled this course...")



# Listing Enrolled Courses
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def MyCourses(request):
    student = StudentProfile.objects.get(user=request.user)
    courses_enrolled = Enrollment.objects.filter(student=student)
    serializer = MycoursesSerializer(courses_enrolled,many=True,context={'request':'request'})
    return Response(serializer.data)



# accessing enrolled courses
class ViewEnrolledCourse(RetrieveAPIView):
    serializer_class = (EnrolledCourseSerializer)
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]




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

