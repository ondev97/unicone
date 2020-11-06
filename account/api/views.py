from rest_framework.generics import CreateAPIView
from .serializer import UserSerializerAPI, TeacherProfileSerializer
from rest_framework.decorators import api_view,permission_classes
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

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def TeacherProfileView(request,pk):
    teacher = TeacherProfile.objects.get(user_id=pk)
    serializer = TeacherProfileSerializer(teacher)
    return Response(serializer.data)