from rest_framework.views import APIView
from rest_framework import parsers, renderers, generics
from rest_framework.compat import coreapi, coreschema
from rest_framework.schemas import ManualSchema
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from database_manager.views import Student, Instructor, TeachingAssistant, Course, ClassEvent
from .serializers import (
    AuthTokenSerializer,
    StudentUserSerializer,
    StudentSerializer,
    InstructorClassEventCoordinatorUserSerializer,
    InstructorSerializer,
    TeachingAssistantClassEventCoordinatorUserSerializer,
    TeachingAssistantSerializer,
    CourseSerializer,
    ClassEventSerializer,
)
from .permissions import (
    DjangoModelPermissionsWithViewPermissionForGET,
    IsStudentForGivenCourse,
    IsInstructorForGivenCourse,
    IsTeachingAssistantForGivenCourse,
)


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


# Student APIs for max depth
# --------------------------


class ListCreateStudentUserView(generics.ListCreateAPIView):
    serializer_class = StudentUserSerializer
    queryset = Student.objects.all()
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


class RetrieveUpdateDestroyStudentUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentUserSerializer
    queryset = Student.objects.all()
    lookup_field = 'entry_number'
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


# Student APIs for min depth
# --------------------------


class CreateStudentView(generics.CreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.none()   # Required for DjangoModelPermissionsWithViewPermissionForGET
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


# Instructor APIs for max depth
# -----------------------------


class ListCreateInstructorClassEventCoordinatorUserView(generics.ListCreateAPIView):
    serializer_class = InstructorClassEventCoordinatorUserSerializer
    queryset = Instructor.objects.all()
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


class RetrieveUpdateDestroyInstructorClassEventCoordinatorUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorClassEventCoordinatorUserSerializer
    queryset = Instructor.objects.all()
    lookup_field = 'instructor_id'
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


# Instructor APIs for medium and min depth
# ----------------------------------------


class CreateInstructorView(generics.CreateAPIView):
    '''
    This view automatically creates `ClassEventCoordinator` object if it doesn't already exist.
    Just the User object needs to exist.
    '''
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.none()    # Required for DjangoModelPermissionsWithViewPermissionForGET
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


# Teaching Assistant APIs for max depth
# -------------------------------------


class ListCreateTeachingAssistantClassEventCoordinatorUserView(generics.ListCreateAPIView):
    serializer_class = TeachingAssistantClassEventCoordinatorUserSerializer
    queryset = TeachingAssistant.objects.all()
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


class RetrieveUpdateDestroyTeachingAssistantClassEventCoordinatorUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeachingAssistantClassEventCoordinatorUserSerializer
    queryset = TeachingAssistant.objects.all()
    lookup_field = 'teaching_assistant_id'
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


# Teaching Assistant APIs for medium and min depth
# ------------------------------------------------


class CreateTeachingAssistantView(generics.CreateAPIView):
    '''
    This view automatically creates `ClassEventCoordinator` object if it doesn't already exist.
    Just the User object needs to exist.
    '''
    serializer_class = TeachingAssistantSerializer
    queryset = TeachingAssistant.objects.none()    # Required for DjangoModelPermissionsWithViewPermissionForGET
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


# Course APIs
# -----------


class ListCreateCourseView(generics.ListCreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


class RetrieveUpdateDestroyCourseView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'code'
    permission_classes = (DjangoModelPermissionsWithViewPermissionForGET,)


# Class Event APIs
# ----------------


class ListClassEventForCourseView(generics.ListAPIView):
    serializer_class = ClassEventSerializer
    permission_classes = (
        IsAuthenticated,
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
    serializer_class = ClassEventSerializer
    permission_classes = (
        IsAuthenticated,
        IsInstructorForGivenCourse|IsTeachingAssistantForGivenCourse,
    )
