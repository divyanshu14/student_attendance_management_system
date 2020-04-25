from rest_framework.views import APIView
from rest_framework import parsers, renderers, generics
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from database_manager.models import(
    Student,
    Instructor,
    TeachingAssistant,
    Course,
    ClassEvent,
    CumulativeAttendance,
)
from .serializers import (
    AuthTokenSerializer,
    UserSerializer,
    StudentUserSerializer,
    StudentSerializer,
    InstructorClassEventCoordinatorUserSerializer,
    InstructorSerializer,
    TeachingAssistantClassEventCoordinatorUserSerializer,
    TeachingAssistantSerializer,
    CourseSerializer,
    CreateUpdateCourseSerializer,
    RestrictedCourseSerializer,
    BasicClassEventSerializer,
    ClassEventForCourseSerializer,
    ClassEventOfStudentForCourseSerializer,
    CumulativeAttendanceForCourseSerializer,
    CumulativeAttendanceOfStudentForCourseSerializer,
)
from .permissions import (
    DjangoModelPermissionsWithViewPermissionForGET,
    GivenCourseExists,
    GivenStudentExists,
    IsGivenStudentRegisteredInGivenCourse,
    IsSameStudentAsGiven,
    IsStudentForGivenCourse,
    IsInstructorForGivenCourse,
    IsTeachingAssistantForGivenCourse,
)


# Auth Token API
# --------------


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer
    if coreapi is not None and coreschema is not None:
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Email address",
                        description="Valid email address for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


obtain_auth_token = ObtainAuthToken.as_view()


# User Data API
# -------------


class GetUserDataView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = UserSerializer(request.user).data
        is_admin = hasattr(request.user, 'admin')
        is_student = hasattr(request.user, 'student')
        is_instructor, is_teaching_assistant = False, False
        if hasattr(request.user, 'classeventcoordinator'):
            is_instructor = hasattr(request.user.classeventcoordinator, 'instructor')
            is_teaching_assistant = hasattr(request.user.classeventcoordinator, 'teachingassistant')
        user_permissions = [str(permission) for permission in request.user.user_permissions.all()]
        role_permissions = []
        for group in request.user.groups.all():
            role_permissions.extend([str(permission) for permission in group.permissions.all()])
        response_data = {
            'user': user,
            'is_admin': is_admin,
            'is_student': is_student,
            'is_instructor': is_instructor,
            'is_teaching_assistant': is_teaching_assistant,
            'user_permissions': user_permissions,
            'role_permissions': role_permissions,
        }
        if is_student:
            student_for_courses = RestrictedCourseSerializer(Course.objects.filter(registered_students=request.user.student), many=True).data
            response_data['student_for_courses'] = student_for_courses
        if is_instructor:
            instructor_for_courses = CourseSerializer(Course.objects.filter(instructors=request.user.classeventcoordinator.instructor), many=True).data
            response_data['instructor_for_courses'] = instructor_for_courses
        if is_teaching_assistant:
            teaching_assistant_for_courses = CourseSerializer(Course.objects.filter(teaching_assistants=request.user.classeventcoordinator.teachingassistant), many=True).data
            response_data['teaching_assistant_for_courses'] = teaching_assistant_for_courses
        return Response(response_data)


# Student APIs for max depth
# --------------------------


class ListCreateStudentUserView(generics.ListCreateAPIView):
    serializer_class = StudentUserSerializer
    queryset = Student.objects.all()
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


class RetrieveUpdateDestroyStudentUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentUserSerializer
    queryset = Student.objects.all()
    lookup_field = 'entry_number'
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


# Student APIs for min depth
# --------------------------


class CreateStudentView(generics.CreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.none()   # Required for DjangoModelPermissionsWithViewPermissionForGET
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


# Instructor APIs for max depth
# -----------------------------


class ListCreateInstructorClassEventCoordinatorUserView(generics.ListCreateAPIView):
    serializer_class = InstructorClassEventCoordinatorUserSerializer
    queryset = Instructor.objects.all()
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


class RetrieveUpdateDestroyInstructorClassEventCoordinatorUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorClassEventCoordinatorUserSerializer
    queryset = Instructor.objects.all()
    lookup_field = 'instructor_id'
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


# Instructor APIs for medium and min depth
# ----------------------------------------


class CreateInstructorView(generics.CreateAPIView):
    '''
    This view automatically creates `ClassEventCoordinator` object if it doesn't already exist.
    Just the User object needs to exist.
    '''
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.none()    # Required for DjangoModelPermissionsWithViewPermissionForGET
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


# Teaching Assistant APIs for max depth
# -------------------------------------


class ListCreateTeachingAssistantClassEventCoordinatorUserView(generics.ListCreateAPIView):
    serializer_class = TeachingAssistantClassEventCoordinatorUserSerializer
    queryset = TeachingAssistant.objects.all()
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


class RetrieveUpdateDestroyTeachingAssistantClassEventCoordinatorUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeachingAssistantClassEventCoordinatorUserSerializer
    queryset = TeachingAssistant.objects.all()
    lookup_field = 'teaching_assistant_id'
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


# Teaching Assistant APIs for medium and min depth
# ------------------------------------------------


class CreateTeachingAssistantView(generics.CreateAPIView):
    '''
    This view automatically creates `ClassEventCoordinator` object if it doesn't already exist.
    Just the User object needs to exist.
    '''
    serializer_class = TeachingAssistantSerializer
    queryset = TeachingAssistant.objects.none()    # Required for DjangoModelPermissionsWithViewPermissionForGET
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


# Course APIs
# -----------


class ListCourseView(generics.ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


class CreateCourseView(generics.CreateAPIView):
    # cannot create new instructors, teaching_assistants and registered_students
    serializer_class = CreateUpdateCourseSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


class RetrieveCourseView(generics.RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'code'
    permission_classes = (
        IsAuthenticated,
        DjangoModelPermissionsWithViewPermissionForGET|IsInstructorForGivenCourse|IsTeachingAssistantForGivenCourse,
    )


class RestrictedRetrieveCourseView(generics.RetrieveAPIView):
    serializer_class = RestrictedCourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'code'
    permission_classes = (
        IsAuthenticated,
        DjangoModelPermissionsWithViewPermissionForGET|IsStudentForGivenCourse|IsInstructorForGivenCourse|IsTeachingAssistantForGivenCourse,
    )


class UpdateCourseView(generics.UpdateAPIView):
    # cannot update instructors, teaching_assistants and registered_students
    serializer_class = CreateUpdateCourseSerializer
    queryset = Course.objects.all()
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


class DestroyCourseView(generics.DestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'code'
    permission_classes = (IsAuthenticated, DjangoModelPermissionsWithViewPermissionForGET,)


# Class Event APIs
# ----------------


class ListClassEventForCourseView(generics.ListAPIView):
    serializer_class = ClassEventForCourseSerializer
    permission_classes = (
        IsAuthenticated,
        GivenCourseExists,
        IsInstructorForGivenCourse|IsTeachingAssistantForGivenCourse,
    )

    def get_queryset(self):
        code = self.kwargs['code']
        queryset = ClassEvent.objects.filter(course__code=code)
        class_event_type = self.request.query_params.get('class_event_type', None)
        attendance_taker_email = self.request.query_params.get('attendance_taker_email', None)
        if class_event_type is not None:
            queryset = queryset.filter(class_event_type=class_event_type)
        if attendance_taker_email is not None:
            queryset = queryset.filter(attendance_taken_by__user__email=attendance_taker_email)
        return queryset


class CreateClassEventForCourseView(generics.CreateAPIView):
    serializer_class = ClassEventForCourseSerializer
    permission_classes = (
        IsAuthenticated,
        GivenCourseExists,
        IsInstructorForGivenCourse|IsTeachingAssistantForGivenCourse,
    )


class ListClassEventOfStudentForCourseView(generics.ListAPIView):
    serializer_class = ClassEventOfStudentForCourseSerializer
    permission_classes = (
        IsAuthenticated,
        GivenCourseExists,
        GivenStudentExists,
        IsGivenStudentRegisteredInGivenCourse,
        IsSameStudentAsGiven|IsInstructorForGivenCourse|IsTeachingAssistantForGivenCourse,
    )

    def get_queryset(self):
        code = self.kwargs['code']
        queryset = ClassEvent.objects.filter(course__code=code)
        class_event_type = self.request.query_params.get('class_event_type', None)
        attendance_taker_email = self.request.query_params.get('attendance_taker_email', None)
        if class_event_type is not None:
            queryset = queryset.filter(class_event_type=class_event_type)
        if attendance_taker_email is not None:
            queryset = queryset.filter(attendance_taken_by__user__email=attendance_taker_email)
        return queryset


# Cumulative Attendance APIs
# --------------------------


class ListCumulativeAttendanceForCourseView(generics.ListAPIView):
    serializer_class = CumulativeAttendanceForCourseSerializer
    permission_classes = (
        IsAuthenticated,
        GivenCourseExists,
        IsInstructorForGivenCourse|IsTeachingAssistantForGivenCourse,
    )

    def get_queryset(self):
        code = self.kwargs['code']
        queryset = CumulativeAttendance.objects.filter(course__code=code)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        extra_data = {}

        if queryset.exists():
            cumulative_attendance_obj = queryset.first()
            # these data elements should be common among all ClassEvent objects having same course attribute
            last_class = BasicClassEventSerializer(cumulative_attendance_obj.last_class).data
            extra_data['last_class'] = last_class
            total_lectures = cumulative_attendance_obj.total_lectures
            extra_data['total_lectures'] = total_lectures
            total_tutorials = cumulative_attendance_obj.total_tutorials
            extra_data['total_tutorials'] = total_tutorials
            total_practicals = cumulative_attendance_obj.total_practicals
            extra_data['total_practicals'] = total_practicals

        response_data = []
        response_data.append(extra_data)
        response_data.append(serializer.data)
        return Response(response_data)


class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field, url_kwarg in zip(self.lookup_fields, self.lookup_url_kwargs):
            if self.kwargs[url_kwarg]: # Ignore empty fields.
                filter[field] = self.kwargs[url_kwarg]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class RetrieveCumulativeAttendanceOfStudentForCourseView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    serializer_class = CumulativeAttendanceOfStudentForCourseSerializer
    queryset = CumulativeAttendance.objects.all()
    lookup_fields = ['course__code', 'student__entry_number']
    lookup_url_kwargs = ['code', 'entry_number']
    permission_classes = (
        IsAuthenticated,
        GivenCourseExists,
        GivenStudentExists,
        IsGivenStudentRegisteredInGivenCourse,
        IsSameStudentAsGiven|IsInstructorForGivenCourse|IsTeachingAssistantForGivenCourse,
    )
