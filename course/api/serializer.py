from rest_framework import serializers
from course.models import Course,Module,Enrollment
from account.models import TeacherProfile



# Serializers for Unauthenticated users


# List all courses

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','course_name','course_cover']


# More info about courses


class CourseDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id','course_name','author','course_cover','course_description']

    def get_author(self, obj):
        return str(obj.author.user.username)

# serializer for authenticated users

# Serializer setup for Creating course and adding modules
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = "__all__"


class CourseCreateSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True)
    read_only = True

    class Meta:
        model = Course
        fields = ['course_name','id','course_description','modules']

    def create(self, validated_data):
        module_data = validated_data.pop('modules')
        course = Course.objects.create(**validated_data)
        for module_data in module_data:
            Module.objects.create(course=course, **module_data)
        return course

    def update(self,instance,validated_data):
        module_data = validated_data.pop('modules')
        course = (instance.modules).all()
        course = list(course)
        print(course)
        instance.course_name = validated_data.get('course_name',instance.course_name)
        instance.course_description = validated_data.get('course_description',instance.course_description)
        instance.save()

        for module_data in module_data:
            module = course.pop(0)
            module.module_name = module_data.get('module_name',module.module_name)
            module.module_content = module_data.get('module_content',module.module_content)
            module.save()
        return instance

# serializer for course Enrollment

class CourseEnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['enroll_key','course','student']