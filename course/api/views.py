from rest_framework.response import Response
from rest_framework.decorators import api_view
from course.models import Course,Module
from account.models import TeacherProfile
from course.api.serializer import (CourseSerializer,
                                   CourseDetailSerializer,
                                   CourseCreateSerializer,
                                   ModuleSerializer)
from rest_framework.generics import( ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView,
                                     RetrieveUpdateAPIView,
                                     ListCreateAPIView)
from rest_framework.permissions import IsAuthenticated

#List courses for unauthenticated users
class ListCourseView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


#creating courses and modules
class CreateCourseView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print("user:-" ,self.request.user)
        teacher = TeacherProfile.objects.get(user=self.request.user.id)
        serializer.save(author=teacher)

#updating courses and modules
class UpdateCourse(RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_classes = [IsAuthenticated]


@api_view(['POST'])
def AddModule(request,pk):
    course = Course.objects.get(id=pk)
    print(course)
    serializer = ModuleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(course=course)
    return Response(serializer.data)

@api_view(['GET',])
def ModuleList(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses,many=True)
    return Response(serializer.data)



