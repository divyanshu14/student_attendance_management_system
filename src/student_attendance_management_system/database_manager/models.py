from django.db import models
from django.contrib.auth.models import Group, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib import auth
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.conf import settings


# every model has inbuilt primary key named id which is AutoField model,
# but many times we want another unique CharField identifier
# Admin.admin_id, Student.entry_number, Instructor.instructor_id,
# TeachingAssistant.teaching_assistant_id, Course.code are such CharField identifiers


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()


class User(AbstractBaseUser, PermissionsMixin):
    '''
    Represents the custom User model.
    '''
    username_validator = UnicodeUsernameValidator()

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Admin(models.Model):
    '''
    Admin class of the Student Attendance Management System.
    Admins are responsible for adding users and assigning roles to them (student or instructor or both)
    and adding courses and assigning instructors, teaching assistants, and students to courses.
    The first admin is given by the Software Manager.
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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


class ClassEventCoordinator(models.Model):
    '''
    Model to represent a class event coordinator.
    Examples of class event coordinators are instructors, teaching assistants, lab attendants.
    '''
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Instructor(ClassEventCoordinator):
    '''
    Model to represent an instructor.
    '''
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


class TeachingAssistant(ClassEventCoordinator):
    '''
    Model to represent a teaching assistant.
    '''
    teaching_assistant_id = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return str(self.teaching_assistant_id) + ' - ' + str(self.user.first_name) + ' ' + str(self.user.last_name)

    def save(self, *args, **kwargs):
        '''
        Avoid bulk saving to ensure that this method gets called.
        '''
        self.teaching_assistant_id = self.teaching_assistant_id.lower()
        ret = super().save(*args, **kwargs)
        teaching_assistants_group = Group.objects.get(name='Teaching Assistants')
        self.user.groups.add(teaching_assistants_group)
        return ret

    def delete(self, *args, **kwargs):
        '''
        Avoid bulk deletion to ensure that this method gets called.
        '''
        ret = super().delete(*args, **kwargs)
        teaching_assistants_group = Group.objects.get(name='Teaching Assistants')
        self.user.groups.remove(teaching_assistants_group)
        return ret


# class LabAttendant(ClassEventCoordinator):
#     '''
#     Model to represent a lab attendant.
#     '''
#     lab_attendant_id = models.CharField(max_length=15, unique=True)

#     def __str__(self):
#         return str(self.lab_attendant_id) + ' - ' + str(self.user.first_name) + ' ' + str(self.user.last_name)

#     def save(self, *args, **kwargs):
#         '''
#         Avoid bulk saving to ensure that this method gets called.
#         '''
#         self.lab_attendant_id = self.lab_attendant_id.lower()
#         ret = super().save(*args, **kwargs)
#         lab_attendants_group = Group.objects.get(name='Lab Attendants')
#         self.user.groups.add(lab_attendants_group)
#         return ret

#     def delete(self, *args, **kwargs):
#         '''
#         Avoid bulk deletion to ensure that this method gets called.
#         '''
#         ret = super().delete(*args, **kwargs)
#         lab_attendants_group = Group.objects.get(name='Lab Attendants')
#         self.user.groups.remove(lab_attendants_group)
#         return ret


class Course(models.Model):
    '''
    Model to represent a course.
    '''
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=10, unique=True)
    relative_attendance_for_one_lecture = models.IntegerField()
    relative_attendance_for_one_tutorial = models.IntegerField()
    relative_attendance_for_one_practical = models.IntegerField()
    instructors = models.ManyToManyField(Instructor)
    teaching_assistants = models.ManyToManyField(TeachingAssistant, blank=True)
    # lab_attendants = models.ManyToManyField(LabAttendant, blank=True)
    registered_students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return str(self.code) + ' - ' + str(self.name)

    def save(self, *args, **kwargs):
        self.code = self.code.lower()
        super().save(*args, **kwargs)


class ClassEvent(models.Model):
    '''
    Model to represent a class event.
    Class event can be one of the three types - lecture, tutorial, practical.
    '''
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    CLASS_EVENT_TYPES = (
        ('L', 'Lecture'),
        ('T', 'Tutorial'),
        ('P', 'Practical')
    )
    class_event_type = models.CharField(max_length=2, choices=CLASS_EVENT_TYPES)
    # LOGIC : enfore that the user must be an Instructor for that Course
    attendance_taken_by = models.ForeignKey(ClassEventCoordinator, on_delete=models.CASCADE)
    # LOGIC : enfore that the user must be a Student registered for that Course
    present_students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return str(self.course) + ' - ' + str(self.timestamp)


class CumulativeAttendance(models.Model):
    '''
    Model to represent the cumulative attendance details of a Student for each Course.
    This is a read-only table for users.
    '''
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    last_class = models.ForeignKey(ClassEvent, on_delete=models.CASCADE)
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