from django.contrib import auth
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .serializer import UserSerializerAPI, TeacherProfileSerializer
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import IsAuthenticated
from ..models import TeacherProfile,User
from rest_framework.response import Response


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
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def TeacherProfileView(request,pk):
    teacher = TeacherProfile.objects.get(user_id=pk)
    serializer = TeacherProfileSerializer(teacher)
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
def TestLoginView(request):
    user = User.objects.get(email=request.data['username'])
    token = None
    try:
        token = Token.objects.get(user=user)
    except:
        pass
    status = False
    if token!=None:
        status = True
    return Response({
        "status" : status
    })