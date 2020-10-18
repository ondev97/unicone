from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from account.api.serializer import TeacherRegSerializer,StudentRegSerializer

@api_view(['POST'])
def registration_view(request):
    serializer = TeacherRegSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save(is_teacher=True)
        data['response'] = "Successfully registered"
        data['email'] = account.email
        data['username'] = account.username
    else:
        data = serializer.errors
    return Response(data)


@api_view(['POST'])
def sturegistration_view(request):
    serializer = StudentRegSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "Successfully registered"
        data['email'] = account.email
        data['username'] = account.username
    else:
        data = serializer.errors
    return Response(data)

