from django.db import models
from django.contrib.auth.models import User


# every model has inbuilt primary key named id which is AutoField model,
# but many times we want another unique CharField identifier
# Admin.admin_id, Student.entry_number, Instructor.instructor_id, Course.code are such CharField identifiers


class Admin(models.Model):
    '''
    Admin class of the Student Attendance Management System.
    Admins are responsible for adding users and assigning roles to them (student or instructor or both)
    and adding courses and assigning instructors, teaching assistants, and students to courses.
    The first admin is given by the Software Manager.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    admin_id = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return str(self.admin_id) + ' - ' + str(self.user)


class Student(models.Model):
    '''
    Model to represent a student.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entry_number = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return str(self.entry_number)


class Instructor(models.Model):
    '''
    Model to represent an instructor.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instructor_id = models.CharField(max_length=15, unique=True)
    def __str__(self):
        return str(self.instructor_id) + ' - ' + str(self.user)


class Course(models.Model):
    '''
    Model to represent a course.
    '''
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=10, unique=True)
    # because of one to one correspondance of User class with Instructor class,
    # we can derive one from the other
    instructors = models.ManyToManyField(User, related_name='instructor_for_courses')
    teaching_assistants = models.ManyToManyField(User, related_name='teaching_assistant_for_courses', blank=True)
    # because of one to one correspondance of User class with Student class,
    # we can derive one from the other
    registered_students = models.ManyToManyField(User, related_name='registered_student_for_courses', blank=True)
    def __str__(self):
        return str(self.code) + ' - ' + str(self.name)


class Class(models.Model):
    '''
    Model to represent a class. Class can be one of the three type - lecture, tutorial, practical.
    '''
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    CLASS_TYPES = (
        ('L', 'Lecture'),
        ('T', 'Tutorial'),
        ('P', 'Practical')
    )
    class_type = models.CharField(max_length=2, choices=CLASS_TYPES)
    attendance_taken_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendance_taken_by_for_classes')
    present_students = models.ManyToManyField(User, related_name='present_student_in_classes', blank=True)
    def __str__(self):
        return str(self.course) + ' - ' + str(self.timestamp)
    class Meta:
        verbose_name_plural = 'Classes'
