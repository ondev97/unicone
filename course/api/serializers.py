from rest_framework import serializers
from course.models import Course
from account.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = TeacherSerializer(
            instance.author).data
        return representation