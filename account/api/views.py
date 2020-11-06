from rest_framework.generics import CreateAPIView
from .serializer import UserSerializerAPI
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class createuser(CreateAPIView):
    serializer_class = UserSerializerAPI

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()

@permission_classes([IsAuthenticated])
def UpdateTeacherProfile(request,pk):
    pass