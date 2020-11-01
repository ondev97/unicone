from rest_framework import serializers
from course.models import Course,Module
from account.models import TeacherProfile


#List all courses for Unauthenticated users
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','course_name','course_description','course_cover']


class CourseDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id','course_name','author','course_cover']
        #fields = ['id', 'course_name', 'add_module', 'author']

    def get_author(self, obj):
        return str(obj.author.user.username)


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"


class CourseCreateSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True)

    class Meta:
        model = Course
        fields = ['course_name','id','course_description','modules']

    def create(self, validated_data):
        module_data = validated_data.pop('modules')
        course = Course.objects.create(**validated_data)
        for module_data in module_data:
            Module.objects.create(course=course, **module_data)
        return course
