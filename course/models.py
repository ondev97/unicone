from django.db import models
from account.models import TeacherProfile,StudentProfile


class Course(models.Model):
    course_name = models.CharField(max_length=300,default=None)
    author = models.ForeignKey(TeacherProfile,on_delete=models.CASCADE,null=True,default=None)
    course_description = models.TextField(null=True)
    course_cover = models.ImageField(null=True,blank=True,upload_to='course_covers/')

    def __str__(self):
        return self.course_name


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True,related_name='modules')
    module_name = models.CharField(max_length=100)
    module_content = models.CharField(max_length=100)

    def __str__(self):
        return self.module_name+ ""+" "+ self.course.course_name

class Enrollment(models.Model):
    name = models.CharField(max_length=100,default="Text here")
    course = models.ForeignKey(Course,models.CASCADE,null=True)
    student = models.ForeignKey(StudentProfile,models.CASCADE,null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = [['course','student']]





