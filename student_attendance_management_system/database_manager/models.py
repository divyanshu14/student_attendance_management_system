from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import pre_delete


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
        return str(self.admin_id) + ' - ' + str(self.user.first_name) + ' ' + str(self.user.last_name)

    def save(self, *args, **kwargs):
        '''
        Avoid bulk saving to ensure that this method gets called.
        '''
        self.admin_id = self.admin_id.lower()
        ret = super().save(*args, **kwargs)
        admins_group = Group.objects.get(name='Admins')
        self.user.groups.add(admins_group)
        return ret

    def delete(self, *args, **kwargs):
        '''
        Avoid bulk deletion to ensure that this method gets called.
        '''
        ret = super().delete(*args, **kwargs)
        admins_group = Group.objects.get(name='Admins')
        self.user.groups.remove(admins_group)
        return ret


class Student(models.Model):
    '''
    Model to represent a student.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entry_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return str(self.entry_number) + ' - ' + str(self.user.first_name) + ' ' + str(self.user.last_name)

    def save(self, *args, **kwargs):
        '''
        Avoid bulk saving to ensure that this method gets called.
        '''
        self.entry_number = self.entry_number.lower()
        ret = super().save(*args, **kwargs)
        students_group = Group.objects.get(name='Students')
        self.user.groups.add(students_group)
        return ret

    def delete(self, *args, **kwargs):
        '''
        Avoid bulk deletion to ensure that this method gets called.
        '''
        ret = super().delete(*args, **kwargs)
        students_group = Group.objects.get(name='Students')
        self.user.groups.remove(students_group)
        return ret


class Instructor(models.Model):
    '''
    Model to represent an instructor.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instructor_id = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return str(self.instructor_id) + ' - ' + str(self.user.first_name) + ' ' + str(self.user.last_name)

    def save(self, *args, **kwargs):
        '''
        Avoid bulk saving to ensure that this method gets called.
        '''
        self.instructor_id = self.instructor_id.lower()
        ret = super().save(*args, **kwargs)
        instructors_group = Group.objects.get(name='Instructors')
        self.user.groups.add(instructors_group)
        return ret

    def delete(self, *args, **kwargs):
        '''
        Avoid bulk deletion to ensure that this method gets called.
        '''
        ret = super().delete(*args, **kwargs)
        instructors_group = Group.objects.get(name='Instructors')
        self.user.groups.remove(instructors_group)
        return ret


class Course(models.Model):
    '''
    Model to represent a course.
    '''
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=10, unique=True)
    relative_attendance_for_one_lecture = models.IntegerField()
    relative_attendance_for_one_tutorial = models.IntegerField()
    relative_attendance_for_one_practical = models.IntegerField()
    # because of one to one correspondance of User class with Instructor class,
    # we can derive one from the other
    # LOGIC : enfore that the user must be an Instructor
    instructors = models.ManyToManyField(
        User, related_name='instructor_for_courses')
    # LOGIC : enfore that the user must be an Instructor
    teaching_assistants = models.ManyToManyField(
        User, related_name='teaching_assistant_for_courses', blank=True)
    # because of one to one correspondance of User class with Student class,
    # we can derive one from the other
    # LOGIC : enfore that the user must be a Student
    registered_students = models.ManyToManyField(
        User, related_name='registered_student_for_courses', blank=True)

    def __str__(self):
        return str(self.code) + ' - ' + str(self.name)

    def save(self, *args, **kwargs):
        self.code = self.code.lower()
        super().save(*args, **kwargs)


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
    # LOGIC : enfore that the user must be an Instructor for that Course
    attendance_taken_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='attendance_taken_by_for_classes')
    # LOGIC : enfore that the user must be a Student registered for that Course
    present_students = models.ManyToManyField(
        User, related_name='present_student_in_classes', blank=True)

    def __str__(self):
        return str(self.course) + ' - ' + str(self.timestamp)

    class Meta:
        verbose_name_plural = 'Classes'


class CumulativeAttendance(models.Model):
    '''
    Model to represent the cumulative attendance details of a Student for each Course.
    This is a read-only table for users.
    '''
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    last_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    was_present_last_class = models.BooleanField()
    total_lectures = models.IntegerField()
    total_tutorials = models.IntegerField()
    total_practicals = models.IntegerField()
    total_lectures_present = models.IntegerField()
    total_tutorials_present = models.IntegerField()
    total_practicals_present = models.IntegerField()

    def __str__(self):
        return str(self.student) + ' - ' + str(self.course)

    class Meta:
        verbose_name_plural = 'Cumulative Attendance'
        constraints = [
            models.UniqueConstraint(
                fields=['student', 'course'], name='Unique Student Registration in Course')
        ]
