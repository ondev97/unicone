from rest_framework import serializers
from account.models import Teacher,Student

class TeacherRegSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Teacher
        fields = ['email', 'username', 'password', 'password2','is_teacher']
        # fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Teacher(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"Passwords must match"})
        account.set_password(password)
        account.save()
        return account


class StudentRegSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Student
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Student(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({"Passwords must match"})
        account.set_password(password)
        account.save()
        return account


from rest_auth.serializers import TokenSerializer
from django.contrib.auth import get_user_model


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model
        fields = ('id', 'email')


class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')

