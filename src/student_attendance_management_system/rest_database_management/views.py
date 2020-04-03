from rest_framework.views import APIView
from django.contrib.auth.models import Group
from django.http import JsonResponse
from database_manager.models import Student, Course, Instructor
from rest_framework.permissions import (
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
	)
from .serializers import ( 
    assignUserToInstructorSerializer,
    assignUserToStudentSerializer, 
    addCourseSerializer, 
    addStudentsSerializer, 
    addInstructorSerializer
)
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.conf import settings

DEFAULT_PASSWORD = "new_pass_123"
from rest_framework.response import Response
import json
from rest_framework.permissions import IsAdminUser


class addStudents(mixins.CreateModelMixin, 
               viewsets.GenericViewSet):
    '''
    Add students
    Exampple POST request 

    [ 
        { "first_name": "amritpal",
            "last_name": "singh",
            "email_address": "amritpal@gmail.com",
            "entry_number": "2017csb106812"},
        { "first_name": "amritpal",
            "last_name": "singh",
            "email_address": "amritpal@gmail.com",
            "entry_number": "2017csb101268"}
    ]

    '''

    serializer_class = addStudentsSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        for single_proportion in serializer.validated_data:
            user = settings.AUTH_USER_MODEL.objects.create_user(
                single_proportion['entry_number'], single_proportion['email_address'], DEFAULT_PASSWORD)
            user.first_name = single_proportion['first_name']
            user.last_name = single_proportion['last_name']
            student_group = Group.objects.get(name='Students')
            user.groups.add(student_group)
            user.save()
            Student.objects.create(user=user, entry_number=single_proportion['entry_number'])
    
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

    
class listStudents(APIView):

    '''
    list all the students
    '''
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        objects = Student.objects.all()
        dictStudents = {}
        index = 1
        for obj in objects:
            dictStudents[index] = {'name': str(obj.user.first_name+" "+obj.user.last_name), 'entry_number': obj.entry_number}
            print(str(obj.user.first_name+" "+obj.user.last_name), '$$$$$$$$')
            index+=1
        print(dictStudents)
        dictStudentsDump = json.dumps(dictStudents)
        jsonStudent = json.loads(dictStudentsDump)
        return Response(jsonStudent)


class addInstructors(mixins.CreateModelMixin, 
               viewsets.GenericViewSet):

    
    '''
    add the instructors
    example input 

    [ 
        { "first_name": "amritpal",
            "last_name": "singh",
            "email_address": "amritpal@gmail.com",
            "instructor_id": "3"},
        { "first_name": "amritpal",
            "last_name": "singh",
            "email_address": "amritpal@gmail.com",
            "instructor_id": "4"}
    ]
    '''    
    serializer_class = addInstructorSerializer
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=False)
        dictErrors = {}
        for single_proportion in serializer.validated_data:
            print(single_proportion['instructor_id'], '$$$$$$$$')

            # create_user takes these fields (username, email, password, **extra_fields)
            user = settings.AUTH_USER_MODEL.objects.create_user(
                single_proportion['instructor_id'], single_proportion['email_address'], DEFAULT_PASSWORD)
            user.first_name = single_proportion['first_name']
            user.last_name = single_proportion['last_name']
            instructor_group = Group.objects.get(name='Instructors')
            user.groups.add(instructor_group)
            user.save()
            Instructor.objects.create(user=user, instructor_id=single_proportion['instructor_id'])
    
        return Response(serializer.errors, status=status.HTTP_201_CREATED)

class listInstructors(APIView):
    
    '''
    list all the instructors
    '''
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        objects = Instructor.objects.all()
        dictInstructor = {}
        index = 1
        for obj in objects:
            dictInstructor[index] = {'name': str(obj.user.first_name+" "+obj.user.last_name), 'instructor_id': obj.instructor_id}
            print(str(obj.user.first_name+" "+obj.user.last_name), '$$$$$$$$')
            index+=1
        print(dictInstructor)
        dictInstructorDump = json.dumps(dictInstructor)
        jsonInstructor = json.loads(dictInstructorDump)
        return Response(jsonInstructor)

class assignUserToStudent(mixins.CreateModelMixin, 
               viewsets.GenericViewSet):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    queryset = Student.objects.all()
    serializer_class = assignUserToStudentSerializer


class assignUserToInstructor(mixins.CreateModelMixin, 
               viewsets.GenericViewSet):
    # authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)

    queryset = Student.objects.all()
    serializer_class = assignUserToInstructorSerializer




# BELOW CODE YET TO BE IMPLEMENTED


"""

{
    "name": "asfasas",
    "code": "asasf",
    "instructor_for_courses": [
                    {"first_name": "3", "last_name": "5", "email_address": "afa@gmail.com", "instructor_id": "3"},
                    {"first_name":"3", "last_name":"5", "email_address": "afa@gmail.com", "instructor_id": "3"}
                    ],

    "relative_attendance_for_one_lecture": 1,
    "relative_attendance_for_one_tutorial": 2,
    "relative_attendance_for_one_practical": 1
}

{
    "name": "asfasas",
    "code": "asasf",
    "instructor_for_courses": [
                    {"first_name": "Balwinder", "last_name": "Sodhi", "email_address": "sodhi@gmail.com", "instructor_id": "1"}
                    ],

    "relative_attendance_for_one_lecture": 1,
    "relative_attendance_for_one_tutorial": 2,
    "relative_attendance_for_one_practical": 1
}

"""

class addCourses(mixins.CreateModelMixin, 
               viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = addCourseSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print(request.data)
        user = settings.AUTH_USER_MODEL.objects.all()
        serializer.is_valid(raise_exception=True)
        instructors = request.data['instructor_for_courses']
        userInstructor = settings.AUTH_USER_MODEL.objects.all().filter(instructors['id'])
        # Course.object.create()

        # user = settings.AUTH_USER_MODEL.object.all()
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)      



"""INPUT THROUGH POST REQUEST

{    
    "things":[
        {"user":"foo1","entry_number":"bar"},
        {"user":"f1oo1","entry_number":"ba2r"}]
}

{    
    "things":[
        { "first_name": "amritpal",
          "last_name": "singh",
          "email_address": "amritpal@gmail.com",
          "entry_number": "2017csb1068"}
     ]
}




"""
# class addStudents(mixins.CreateModelMixin, viewsets.GenericViewSet):
#     queryset = Student.objects.all()
#     serializer_class = addStudentsSerializer

    # def create(self, request, *args, **kwargs):
    #     self.user = request.user
    #     listOfThings = request.data['things']
    #     print(listOfThings)
    #     serializer = self.get_serializer(data=listOfThings, many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         headers = self.get_success_headers(serializer.data)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED,
    #                         headers=headers)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
INPUT THROUGH POPST REQUEST

[
    {"user":"foo1","entry_number":"bar"},
    {"user":"f1oo1","entry_number":"ba2r"}
]

# class addStudents(mixins.CreateModelMixin, viewsets.GenericViewSet):
#     model = Student
#     queryset = model.objects.all()
#     serializer_class = addStudentsSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)      
"""