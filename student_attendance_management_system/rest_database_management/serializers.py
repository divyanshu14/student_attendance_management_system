from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from database_manager.models import Student, Course, Instructor
from django.contrib.auth.models import User, Group
import random
DEFAULT_PASSWORD = "new_pass_123"

class addStudentsSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100, write_only=True)
    last_name = serializers.CharField(max_length=100,  write_only=True)
    email_address = serializers.EmailField( write_only=True)

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email_address', 'entry_number')


class addInstructorSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100, write_only=True)
    last_name = serializers.CharField(max_length=100,  write_only=True)
    email_address = serializers.EmailField( write_only=True)

    class Meta:
        model = Instructor
        fields = ('first_name', 'last_name', 'email_address', 'instructor_id')
        
class addCourseSerializer(serializers.ModelSerializer):
    instructor_for_courses = addInstructorSerializer(many=True)
    # exclude = ('first_name', 'last_name', 'email_address')
        
    # instructor_for_courses = serializers.StringRelatedField(many=True, write_only=True)

    class Meta:
        model = Course
        fields = ('name', 'code', 'instructor_for_courses' ,'relative_attendance_for_one_lecture', 'relative_attendance_for_one_tutorial', 'relative_attendance_for_one_practical')
        
class assignUserToStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user', 'entry_number')

class assignUserToInstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('user', 'entry_number')