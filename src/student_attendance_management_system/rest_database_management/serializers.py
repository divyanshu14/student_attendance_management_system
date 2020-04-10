from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
)
from database_manager.models import Student, Course, Instructor, TeachingAssistant
from django.contrib.auth.models import Group
import random

DEFAULT_PASSWORD = "new_pass_123"


class addStudentsSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100, write_only=True)
    last_name = serializers.CharField(max_length=100,  write_only=True)
    email_address = serializers.EmailField(write_only=True)

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
        

class addTeachingAssistantSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=100, write_only=True)
    last_name = serializers.CharField(max_length=100, write_only=True)
    email_address = serializers.EmailField()
    class Meta:
        model = TeachingAssistant
        fields = ('first_name', 'last_name', 'email_address', 'teaching_assistant_id')


class addCourseSerializer(serializers.ModelSerializer):
    instructor_ids = serializers.ListField(child=serializers.CharField(max_length=100, write_only=True), write_only=True)
    student_ids = serializers.ListField(child=serializers.CharField(max_length=100, write_only=True), write_only=True)
    teaching_assistant_ids = serializers.ListField(child=serializers.CharField(max_length=100, write_only=True), write_only=True)
    # students_ids = 
    # teaching_assistants_ids = 

    class Meta:
        model = Course
        fields = ('name', 'code', 'instructor_ids', 'teaching_assistant_ids', 'student_ids' ,'relative_attendance_for_one_lecture', 'relative_attendance_for_one_tutorial', 'relative_attendance_for_one_practical')
        
    # def save(self):

    #     # dict_errors = []
    #     print("######################################")
        
    #     return self.serializer.validated_data


class assignStudentToUserSerializer(serializers.ModelSerializer):
    email_address = serializers.EmailField(write_only=True)
    class Meta:
        model = Student
        fields = ('email_address', 'entry_number')


class assignInstructorToUserSerializer(serializers.ModelSerializer):
    email_address = serializers.EmailField(write_only=True)
    class Meta:
        model = Instructor
        fields = ('email_address', 'instructor_id')


class assignInstructorToClassEventCoordinatorSerializer(serializers.ModelSerializer):
    pass


class assignTeachingAssistantToUserSerializer(serializers.ModelSerializer): 
    email_address = serializers.EmailField(write_only=True)
    class Meta:
        model = TeachingAssistant
        fields = ('email_address', 'teaching_assistant_id')


class assignTeachingAssistantToClassEventCoordinatorSerializer(serializers.ModelSerializer):
    pass
