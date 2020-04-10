from rest_framework.views import APIView
from django.contrib.auth.models import Group
from django.http import JsonResponse
from database_manager.models import (
    Student,
    Course, 
    Instructor,
    TeachingAssistant,
    ClassEventCoordinator
)
from rest_framework.permissions import (
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
	)
from .serializers import ( 
    assignInstructorToUserSerializer,
    assignStudentToUserSerializer, 
    addCourseSerializer, 
    addStudentsSerializer, 
    addInstructorSerializer,
    assignTeachingAssistantToUserSerializer,
    addTeachingAssistantSerializer
)
import database_manager.models as dbModels
from rest_framework import viewsets, mixins, status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import SessionAuthentication

DEFAULT_PASSWORD = "new_pass_123"
import json
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        User = dbModels.User
        user = get_object_or_404(User, email=token.user.email)
        # user = dbModels.User.objects.all().filter(email=token.user.email)[0]
        first_name = user.first_name
        last_name = user.last_name
        is_student = False
        is_teacher = False
        is_ta = False
        if Student.objects.all().filter(user=user):
            is_student = True
        try:
            class_event_coordinator = ClassEventCoordinator.objects.all().filter(user=user)[0]
            # class_event_coordinator = get_object_or_404(ClassEventCoordinator, user=user)
        except:
            return Response({'token': token.key,
                         'username': token.user.email,
                         'admin_permissions': token.user.is_staff,
                         'first_name': first_name,
                         'last_name': last_name,
                         'is_student': is_student,
                         'is_teacher': False,
                         'is_ta': False
                         })
 
        if Instructor.objects.all().filter(class_event_coordinator=class_event_coordinator):
            is_teacher = True
        if TeachingAssistant.objects.all().filter(class_event_coordinator=class_event_coordinator):
            is_ta = True
        
        return Response({'token': token.key,
                         'username': token.user.email,
                         'admin_permissions': token.user.is_staff,
                         'first_name': first_name,
                         'last_name': last_name,
                         'is_student': is_student,
                         'is_teacher': is_teacher,
                         'is_ta': is_ta
                         })


class addStudents(mixins.CreateModelMixin, 
               viewsets.GenericViewSet):
    '''
    Add students
    Exampple POST request 

    [ 
        { "first_name": "Shivam",
            "last_name": "Prasad",
            "email_address": "2017csb1110@iitrpr.ac.in",
            "entry_number": "2017csb1101"},
        { "first_name": "amritpal",
            "last_name": "singh",
            "email_address": "amritpal@gmail.com",
            "entry_number": "2017csb101268"}
    ]


    '''

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    serializer_class = addStudentsSerializer
    queryset = Student.objects.all()
    def create(self, request, *args, **kwargs):
        UserModel = dbModels.User
        self.serializer = self.get_serializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        errors = []
        for single_proportion in self.serializer.validated_data:
            info = {}
            try:
                user = UserModel.objects.create_user(single_proportion['email_address'], DEFAULT_PASSWORD)
                user.first_name = single_proportion['first_name']
                user.last_name = single_proportion['last_name']
                student_group = Group.objects.get(name='Students')
                user.groups.add(student_group)
                user.save()
                Student.objects.create(user=user, entry_number=single_proportion['entry_number'])
            except:
                info = {single_proportion['email_address']: "User Cannot be created"}
                errors.append(info)
            
                print(errors, self.serializer.errors)
        x = 0
        for i in errors:
            if(i != {}):
                x = 1
        if x == 1:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer.validated_data, status=status.HTTP_201_CREATED)

    
class listStudents(APIView):

    '''
    list all the students
    '''
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = Student.objects.all()
    def get(self, request, *args, **kwargs):
        objects = Student.objects.all()
        dictStudents = {}
        index = 1
        for obj in objects:
            dictStudents[index] = {'name': str(obj.user.first_name+" "+obj.user.last_name),'email': str(obj.user.email), 'entry_number': obj.entry_number}
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
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    serializer_class = addInstructorSerializer
    queryset = Instructor.objects.all()
    def create(self, request, *args, **kwargs):
        UserModel = dbModels.User
        self.serializer = self.get_serializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        errors = []
        
        for single_proportion in self.serializer.validated_data:
            info = {}
            # create_user takes these fields (username, email, password, **extra_fields)
            try:
                user = UserModel.objects.create_user(single_proportion['email_address'], DEFAULT_PASSWORD)    
                user.first_name = single_proportion['first_name']
                user.last_name = single_proportion['last_name']
                instructor_group = Group.objects.get(name='Instructors')
                user.groups.add(instructor_group)
                user.save()
                class_event_coordinator = ClassEventCoordinator.objects.create(user=user)            
                Instructor.objects.create(class_event_coordinator=class_event_coordinator, instructor_id=single_proportion['instructor_id'])
                errors.append({})
            except:
                info = {single_proportion['email_address']: "User Cannot be created, Check if The Group exists or not Or if User already exists"}
                errors.append(info)
            
        print(errors, self.serializer.errors)
        x = 0
        for i in errors:
            if(i != {}):
                x = 1
        if x == 1:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer.validated_data, status=status.HTTP_201_CREATED)



class addTeachingAssistant(mixins.CreateModelMixin, 
                viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = TeachingAssistant.objects.all()
    serializer_class = addTeachingAssistantSerializer
    def create(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        errors = []
        index = 0
        for single_proportion in self.serializer.validated_data:
            info = {}
            try:
                user = dbModels.User.objects.create_user(single_proportion['email_address'], DEFAULT_PASSWORD)
                user.first_name = single_proportion['first_name']
                user.last_name = single_proportion['last_name']
                ta_group = Group.objects.get(name='Teaching Assistants')
                user.groups.add(ta_group)
                user.save()
                class_event_coordinator = ClassEventCoordinator.objects.create(user=user)
                TeachingAssistant.objects.create(class_event_coordinator=class_event_coordinator, teaching_assistant_id=single_proportion['teaching_assistant_id'])
                errors.append({})
            except:
                info = {single_proportion['email_address']: "User Cannot be created"}
                errors.append(info)
            
                print(errors, self.serializer.errors)
        x = 0
        for i in errors:
            if(i != {}):
                x = 1
        if x == 1:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(self.serializer.validated_data, status=status.HTTP_201_CREATED)

class listInstructors(APIView):
    
    '''
    list all the instructors
    '''
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = Instructor.objects.all()
    def get(self, request, *args, **kwargs):
        objects = Instructor.objects.all()
        dictInstructor = {}
        index = 1
        for obj in objects:
            dictInstructor[index] = {
                'name': str(obj.class_event_coordinator.user.first_name+" "+obj.class_event_coordinator.user.last_name),
                'instructor_id': str(obj.instructor_id),
                'email': str(obj.class_event_coordinator.user.email)}
            index+=1
        print(dictInstructor)
        dictInstructorDump = json.dumps(dictInstructor)
        jsonInstructor = json.loads(dictInstructorDump)
        return Response(jsonInstructor)

class listTeachingAssistant(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = TeachingAssistant.objects.all()

    def get(self, request, *args, **kwargs):
        objects = TeachingAssistant.objects.all()
        dictTA = {}
        index = 1
        for obj in objects:
            dictTA[index] = {
                'name': str(obj.class_event_coordinator.user.first_name+" "+obj.class_event_coordinator.user.last_name),
                'instructor_id': str(obj.teaching_assistant_id)}
            index+=1
        print(dictTA)
        dictTADump = json.dumps(dictTA)
        jsonTA = json.loads(dictTADump)
        return Response(jsonTA)



class assignStudentToUser(mixins.CreateModelMixin, 
               viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    UserModel = dbModels.User
    queryset = Student.objects.all()
    serializer_class = assignStudentToUserSerializer

    def create(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        errors = []
        for single_proportion in self.serializer.validated_data:
            try:
                info = {}
                email_address = single_proportion['email_address']
                entry_number = single_proportion['entry_number']
                user = dbModels.User.objects.all().filter(email=email_address)[0]
                student_group = Group.objects.get(name='Students')
                user.groups.add(student_group)
                user.save()
                Student.objects.create(user=user, entry_number=entry_number)
            except:
                info = {single_proportion['email_address']: 'Error Saving this User, Check if the Groups and User Exist or Not'}
                errors.append(info)

                print(errors, self.serializer.errors)
        x = 0
        for i in errors:
            if(i != {}):
                x = 1
        if x == 1:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer.validated_data, status=status.HTTP_201_CREATED)   

class assignInstructorToUser(mixins.CreateModelMixin, 
               viewsets.GenericViewSet):
    UserModel = dbModels.User
    
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = Instructor.objects.all()
    serializer_class = assignInstructorToUserSerializer
    
    def create(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        errors = []
        for single_proportion in self.serializer.validated_data:   
            info = {}
            try:
                email_address = single_proportion['email_address']
                instructor_id = single_proportion['instructor_id']
                user = dbModels.User.objects.all().filter(email=email_address)[0]
                instructor_group = Group.objects.get(name='Instructors')
                user.groups.add(instructor_group)
                user.save()
                class_event_coordinator, created = ClassEventCoordinator.objects.get_or_create(user=user)
                Instructor.objects.create(class_event_coordinator=class_event_coordinator, instructor_id=instructor_id)
 
            except:
                info = {single_proportion['email_address']: 'Error Saving this User, Check if the Groups and User Exist or Not'}
                errors.append(info)

                print(errors, self.serializer.errors)
        x = 0
        for i in errors:
            if(i != {}):
                x = 1
        if x == 1:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer.validated_data, status=status.HTTP_201_CREATED)   



class assignInstructorToClassEventCoordinator(mixins.CreateModelMixin, 
                viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = Instructor.objects.all()
    serializer_class = assignInstructorToUserSerializer # i can use the same.
    
    def create(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        errors = []
        for single_proportion in self.serializer.validated_data:
            info = {}
            try:
                email_address = single_proportion['email_address']
                instructor_id = single_proportion['instructor_id']
                instructor_group = Group.objects.get(name='Instructors')
                user = dbModels.User.objects.all().filter(email=email_address)[0]
                # class_event_coordinator = dbModels.ClassEventCoordinator.objects.create(user=user)
                user.groups.add(instructor_group)
                user.save()
                class_event_coordinator, created = ClassEventCoordinator.objects.get_or_create(user=user)
                Instructor.objects.create(class_event_coordinator=class_event_coordinator, instructor_id=instructor_id)
            except:
                info = {single_proportion['email_address']: 'Error Saving this User, Check if the Groups and User Exist or Not'}
                errors.append(info)

                print(errors, self.serializer.errors)
        x = 0
        for i in errors:
            if(i != {}):
                x = 1
        if x == 1:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer.validated_data, status=status.HTTP_201_CREATED)   
                


class assignTeachingAssistantToClassEventCoordinator(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = Instructor.objects.all()
    serializer_class = assignTeachingAssistantToUserSerializer # i can use the same.
    
    def create(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        errors = []
        for single_proportion in self.serializer.validated_data:
            info = {}
            try:
                email_address = single_proportion['email_address']
                teaching_assistant_id = single_proportion['teaching_assistant_id']
                ta_group = Group.objects.get(name='Teaching Assistants')
                user = dbModels.User.objects.all().filter(email=email_address)[0]
                user.groups.add(ta_group)
                user.save()
                class_event_coordinator, created = ClassEventCoordinator.objects.get_or_create(user=user)
                TeachingAssistant.objects.create(class_event_coordinator=class_event_coordinator, teaching_assistant_id=teaching_assistant_id)

            except:
                info = {single_proportion['email_address']: 'Error Saving this User, Check if the Groups and User Exist or Not'}
                errors.append(info)

                print(errors, self.serializer.errors)
        x = 0
        for i in errors:
            if(i != {}):
                x = 1
        if x == 1:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer.validated_data, status=status.HTTP_201_CREATED)   
               

class assignTeachingAssistantToUser(mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = TeachingAssistant.objects.all()
    serializer_class = assignTeachingAssistantToUserSerializer # i can use the same.
    
    def create(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        errors = []
        for single_proportion in self.serializer.validated_data:
            info = {}
            try:
                email_address = single_proportion['email_address']
                teaching_assistant_id = single_proportion['teaching_assistant_id']
                ta_group = Group.objects.get(name='Teaching Assistants')
                user = dbModels.User.objects.all().filter(email=email_address)[0]
                # ClassEventCoordinator = dbModels.ClassEventCoordinator.objects.all(user=user)
                user.groups.add(ta_group)
                user.save()
                class_event_coordinator, created = ClassEventCoordinator.objects.get_or_create(user=user)
                TeachingAssistant.objects.create(class_event_coordinator=class_event_coordinator, teaching_assistant_id=teaching_assistant_id)
            except:
                info = {single_proportion['email_address']: 'Error Saving this User, Check if the Groups and User Exist or Not'}
                errors.append(info)

                print(errors, self.serializer.errors)
        x = 0
        for i in errors:
            if(i != {}):
                x = 1
        if x == 1:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.serializer.validated_data, status=status.HTTP_201_CREATED)   
           



class addCourses(mixins.CreateModelMixin,
                viewsets.GenericViewSet):
    """
    [{
    "name": "Networking",
    "code": "cs304",
    "instructor_ids": ["sodhi@iitrpr.ac.in", "harpal@gmail.com"],
    "teaching_assistant_ids": ["karan69@gmail.com"],
    "student_ids": ["2017csb1068@gmail.com", "2017csb1068@gmail.com"],
    "relative_attendance_for_one_lecture": 1,
    "relative_attendance_for_one_tutorial": 1,
    "relative_attendance_for_one_practical": 1
    }]
    """
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)

    queryset = Course.objects.all()
    serializer_class = addCourseSerializer
    
    def create(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=request.data, many=True)
        self.serializer.is_valid(raise_exception=True)
        errors = []
        for single_proportion in self.serializer.validated_data:
            info = {}
            instructors = single_proportion['instructor_ids']
            ta_ids = single_proportion['teaching_assistant_ids']
            student_ids = single_proportion['student_ids']
            name = single_proportion['name']
            code = single_proportion['code']
            ra_lecture = single_proportion['relative_attendance_for_one_lecture']
            ra_tutorial = single_proportion['relative_attendance_for_one_tutorial']
            ra_practical = single_proportion['relative_attendance_for_one_practical']
            print("################")
            print(instructors)
            print(ta_ids)
            print(student_ids)
            print("################")
            instructor_not_found = []
            ta_not_found = []
            student_not_found = []
            for i in range(len(instructors)):
                if not Instructor.objects.all().filter(instructor_id=str(instructors[i])):
                    instructor_not_found.append(instructors[i])

            
            for i in range(len(ta_ids)):
                if not TeachingAssistant.objects.filter(teaching_assistant_id=ta_ids[i]):
                    ta_not_found.append(ta_ids[i])


            for i in range(len(student_ids)):
                if not Student.objects.filter(entry_number=student_ids[i]):
                    student_not_found.append(student_ids[i])
            
            if(len(instructor_not_found) or len(ta_not_found) or len(student_not_found)):
                info['instructors'] = str(instructor_not_found) + " These Instructors Were Not Found"  
                info['teaching_assistant'] = str(ta_not_found) + "These TAs were not found"
                info['Students'] = str(student_not_found) + "These Students were not Found"
                errors.append(info)
                continue
            else:
                errors.append({})

            course = Course.objects.create(code=code, name=name, 
                            relative_attendance_for_one_lecture=ra_lecture,
                            relative_attendance_for_one_tutorial=ra_tutorial,
                            relative_attendance_for_one_practical=ra_practical)
            for id in instructors:
                instructor = Instructor.objects.all().filter(instructor_id=id)[0]
                course.instructors.add(instructor)
            
            for id in student_ids:
                student = Student.objects.all().filter(entry_number=id)[0]
                course.registered_students.add(student)
            
            for id in ta_ids:
                ta = TeachingAssistant.objects.all().filter(teaching_assistant_id=id)[0]
                course.teaching_assistants.add(ta)
                print(errors, self.serializer.errors)
        x = 0
        for i in errors:
            if(i != {}):
                x = 1
        if x == 1:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
            
        return Response(self.serializer.data, status=status.HTTP_201_CREATED)


class listCourses(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, IsAuthenticated)
    queryset = Course.objects.all()
    def get(self, request, *args, **kwargs):
        objects = Course.objects.all()
        dictCourse = {}
        index = 1
        for obj in objects:
            dictCourse[index] = {
                'name': str(obj.name),
                'code': str(obj.code),
                'relative_attendance_for_one_lecture': str(obj.relative_attendance_for_one_lecture),
                'relative_attendance_for_one_tutorial': str(obj.relative_attendance_for_one_tutorial),
                'relative_attendance_for_one_practical': str(obj.relative_attendance_for_one_practical),
                'instructors': str([instructor.instructor_id for instructor in obj.instructors.all()]),
                'teaching assistant': str([ta.teaching_assistant_id for ta in obj.teaching_assistants.all()]),
                'students': str([rs.entry_number for rs in obj.registered_students.all()]),
            }
            index+=1
        dictCourseDump = json.dumps(dictCourse)
        jsonCourse = json.loads(dictCourseDump)
        return Response(jsonCourse)





# BELOW CODE is OLD CODE JUST FOR HELP .


"""

{
    "name": "asfasas",
    "code": "asasf",
    "instructor_for_courses": [
                    {"instructor_id": "3"},
                    {"instructor_id": "3"}
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
