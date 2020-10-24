from rest_auth.serializers import TokenSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializerAPI(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password','is_teacher']
        extra_kwargs = {"password":{"write_only":True}}

        # def create(self,validated_data):
        #     username = validated_data['username']
        #     email = validated_data['email']
        #     password = validated_data['password']
        #     user_obj = User(
        #         username = username,
        #         email = email
        #     )
        #     user_obj.set_password(password)
        #     user_obj.save()
        #     return user_obj
        # def create(self,validated_data):
        #     user = User.objects.create(
        #         email = validated_data['email'],
        #         username = validated_data['username'],
        #         password = make_password(validated_data['password'])
        #     )
        #
        #     user.save()
        #     return user
        #


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email','is_teacher')


class CustomTokenSerializer(TokenSerializer):
    user = UserTokenSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')

