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
    enroll_key = models.CharField(max_length=100,default="Text here",null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True,related_name='enrollment')
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.course.course_name

    # class Meta:
    #     unique_together = [['course','student']]

# sandeep+django=sadneepdajngo
# coupenStr = student + ":" + course
# coupen = encrypt(coupenStr, key="lms")

#Coupen table ( student, course, coupen )

    #view
    #   str = decrypt(request.data.coupen, key="lms").split(':')
    #   course = Course.obejects.filter(ie__exact == str[1])
    #   if str[0] == request.user.username and  str[1] ==  pk
    #       .......................

# hf
# enroll view
#coursestr.split()
#course name = enrolling course.name
#studtn name = student.name

