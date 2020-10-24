# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from course.models import Course
# from account.models import Teacher
# from course.api.serializers import CourseSerializer
# from .serializers import CourseSerializer
#
#
# @api_view(['GET', ])
# def courselist(request):
#     courses = Course.objects.all()
#     serializer = CourseSerializer(courses, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def createcourse(request):
#     user = request.user
#     author = Teacher.objects.get(username=user.username)
#     serializer = CourseSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(author=author)
#     return Response(serializer.data)
#
#
