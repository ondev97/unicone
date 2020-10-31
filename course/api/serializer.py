from rest_framework import serializers
from course.models import Course,Module
from account.models import TeacherProfile


#List all courses for Unauthenticated users
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','course_name','course_description','course_cover']


#course detail view serializer


#course create serializer
class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name','course_description','course_cover']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'


class CreateModuleSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True)
    class Meta:
        model = Course
        fields = ['course_name','modules']

    def create(self,validated_data):
        modules_data = validated_data.pop('modules')
        course = Course.objects.create(**validated_data)
        for modules_data in modules_data:
            Module.objects.create(course=course,**modules_data)
        return course

class CourseDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    modules = ModuleSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id','course_name','author','modules']
        #fields = ['id', 'course_name', 'add_module', 'author']

    def get_author(self, obj):
        return str(obj.author.user.username)
