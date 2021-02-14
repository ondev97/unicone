from django.contrib import auth
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .filters import StudentFilter
from .serializer import UserSerializerAPI, TeacherProfileSerializer,StudentProfileSerializer
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from ..models import TeacherProfile,User,StudentProfile
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.core.mail import send_mail
from django.conf import settings
from course.models import Enrollment



# Create your views here.

class createuser(CreateAPIView):
    serializer_class = UserSerializerAPI

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

# Logout View
class LogoutView(APIView):
    @staticmethod
    def delete(request, *args, **kwargs):
        request.user.auth_token.delete()
        data = {
            "message": "You have successfully logged out.",
        }
        return Response(data)


# Retrieve User profile of Teacher
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TeacherProfileView(request,pk):
    teacher = TeacherProfile.objects.get(user_id=pk)
    serializer = TeacherProfileSerializer(teacher)
    serializer.data['user'].pop('password')
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def StudentProfileView(request,pk):
    student = StudentProfile.objects.get(user_id=pk)
    serializer = StudentProfileSerializer(student)
    serializer.data['user'].pop('password')
    return Response(serializer.data)




# Update User profile of Teacher

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser,FormParser])
def UpdateTeacherProfileView(request,pk):
    teacher = TeacherProfile.objects.get(user_id=pk)
    serializer = TeacherProfileSerializer(instance=teacher,data=request.data)
    if serializer.is_valid():
        serializer.save()
        serializer.data['user'].pop('password')
        #print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser,FormParser])
def UpdateStudentProfileView(request,pk):
    student = StudentProfile.objects.get(user_id=pk)
    serializer = StudentProfileSerializer(instance=student,data=request.data)
    if serializer.is_valid():
        serializer.save()
        serializer.data['user'].pop('password')
        #print(serializer.data)
    return Response(serializer.data)



@api_view(['POST'])
def TestLoginView(request):
    user = User.objects.filter(email=request.data['username']).first()
    status = False
    if not user:
        return Response({
            "status": status
        })
    token = Token.objects.filter(user=user).first()
    if token:
        status = True
    return Response({
        "status" : status
    })

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def UpdateUser(request,pk):
#     user = User.objects.get(id=pk)
#     print(user.password)
#     dic = request.data
#     dic['password'] = user.password
#     serializer = UserSerializerAPI(instance=user,data=dic)
#     if serializer.is_valid():
#         print("valid")
#         serializer.save()
#     return Response (serializer.data)

class UpdateUser(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializerAPI
    queryset = User.objects.all()

    def perform_update(self, serializer):
        if self.request.user.check_password(self.request.data['password']):
            instance = serializer.save()
            print(instance.password)
            instance.set_password(instance.password)
            instance.save()
        else:
            print("not matched")
            raise APIException("Password's not matching")


@api_view(['GET'])
def Allteachers(request):
    teachers = TeacherProfile.objects.all()
    teachers_list = sorted(teachers, key=lambda x: x.user.first_name, reverse=False)
    serializer = TeacherProfileSerializer(teachers_list,many=True)
    for i in range(len(serializer.data)):
        serializer.data[i]['user'].pop('password')
    return Response(serializer.data)


# class ContactForm(APIView):
#     def post(self, request, *args, **kwargs):
#          serailizer_class = ContactForm(data=request.data)
#          if serailizer_class.is_valid():
#              data = serailizer_class.validated_data
#              email_from = data.get('email')
#              subject = data.get('subject')
#              message = data.get('message')
#              send_mail(subject, message, email_from,['navanjane@zohomail.com'],)
#
#          return Response({"success": "Sent"})
#          return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)


from django.contrib import auth
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .filters import StudentFilter
from .serializer import UserSerializerAPI, TeacherProfileSerializer,StudentProfileSerializer
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from ..models import TeacherProfile,User,StudentProfile
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.core.mail import send_mail
from django.conf import settings
from course.models import Enrollment



# Create your views here.

class createuser(CreateAPIView):
    serializer_class = UserSerializerAPI

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

# Logout View
class LogoutView(APIView):
    @staticmethod
    def delete(request, *args, **kwargs):
        request.user.auth_token.delete()
        data = {
            "message": "You have successfully logged out.",
        }
        return Response(data)


# Retrieve User profile of Teacher
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TeacherProfileView(request,pk):
    teacher = TeacherProfile.objects.get(user_id=pk)
    serializer = TeacherProfileSerializer(teacher)
    serializer.data['user'].pop('password')
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def StudentProfileView(request,pk):
    student = StudentProfile.objects.get(user_id=pk)
    serializer = StudentProfileSerializer(student)
    serializer.data['user'].pop('password')
    return Response(serializer.data)




# Update User profile of Teacher

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser,FormParser])
def UpdateTeacherProfileView(request,pk):
    teacher = TeacherProfile.objects.get(user_id=pk)
    serializer = TeacherProfileSerializer(instance=teacher,data=request.data)
    if serializer.is_valid():
        serializer.save()
        serializer.data['user'].pop('password')
        #print(serializer.data)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser,FormParser])
def UpdateStudentProfileView(request,pk):
    student = StudentProfile.objects.get(user_id=pk)
    serializer = StudentProfileSerializer(instance=student,data=request.data)
    if serializer.is_valid():
        serializer.save()
        serializer.data['user'].pop('password')
        #print(serializer.data)
    return Response(serializer.data)



@api_view(['POST'])
def TestLoginView(request):
    user = User.objects.filter(email=request.data['username']).first()
    status = False
    if not user:
        return Response({
            "status": status
        })
    token = Token.objects.filter(user=user).first()
    if token:
        status = True
    return Response({
        "status" : status
    })

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def UpdateUser(request,pk):
#     user = User.objects.get(id=pk)
#     print(user.password)
#     dic = request.data
#     dic['password'] = user.password
#     serializer = UserSerializerAPI(instance=user,data=dic)
#     if serializer.is_valid():
#         print("valid")
#         serializer.save()
#     return Response (serializer.data)

class UpdateUser(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializerAPI
    queryset = User.objects.all()

    def perform_update(self, serializer):
        if self.request.user.check_password(self.request.data['password']):
            instance = serializer.save()
            print(instance.password)
            instance.set_password(instance.password)
            instance.save()
        else:
            print("not matched")
            raise APIException("Password's not matching")


@api_view(['GET'])
def Allteachers(request):
    teachers = TeacherProfile.objects.all()
    teachers_list = sorted(teachers, key=lambda x: x.user.first_name, reverse=False)
    serializer = TeacherProfileSerializer(teachers_list,many=True)
    for i in range(len(serializer.data)):
        serializer.data[i]['user'].pop('password')
    return Response(serializer.data)


# class ContactForm(APIView):
#     def post(self, request, *args, **kwargs):
#          serailizer_class = ContactForm(data=request.data)
#          if serailizer_class.is_valid():
#              data = serailizer_class.validated_data
#              email_from = data.get('email')
#              subject = data.get('subject')
#              message = data.get('message')
#              send_mail(subject, message, email_from,['navanjane@zohomail.com'],)
#
#          return Response({"success": "Sent"})
#          return Response({'success': "Failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def GetStudents(request, id):
    enr = Enrollment.objects.filter(course_id=id)
    enrollments = []
    for e in enr:
        enrollments.append(e.student.id)
    students = StudentProfile.objects.exclude(id__in=enrollments)
    filterset = StudentFilter(request.GET, queryset=students)
    if filterset.is_valid():
        queryset = filterset.qs
        paginator = PageNumberPagination()
        paginator.page_size = 3
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = StudentProfileSerializer(result_page, many=True)
        for i in range(len(serializer.data)):
            serializer.data[i]['user'].pop('password')
        return paginator.get_paginated_response(serializer.data)






@api_view(['POST'])
def ContactForm(request):
    message = request.data['message']
    name = request.data['name']
    subject = request.data['subject']
    phone_no = request.data['phone_number']
    email_from = request.data['email']


    message = 'From : ' + email_from + '\nName : ' + name + '\nPhone No. : ' + phone_no + '\n\n' + message
    email_to = ['nkindelpitiya@gmail.com']
    send_mail(subject, message, settings.EMAIL_HOST_USER, email_to, fail_silently=False)
    return Response({"message":"Email was sent successfully"}, status=200)





@api_view(['POST'])
def ContactForm(request):
    message = request.data['message']
    name = request.data['name']
    subject = request.data['subject']
    phone_no = request.data['phone_number']
    email_from = request.data['email']


    message = 'From : ' + email_from + '\nName : ' + name + '\nPhone No. : ' + phone_no + '\n\n' + message
    email_to = ['nkindelpitiya@gmail.com']
    send_mail(subject, message, settings.EMAIL_HOST_USER, email_to, fail_silently=False)
    return Response({"message":"Email was sent successfully"}, status=200)