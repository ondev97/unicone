from rest_framework.generics import CreateAPIView
from .serializer import UserSerializerAPI


# Create your views here.

class createuser(CreateAPIView):
    serializer_class = UserSerializerAPI

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()