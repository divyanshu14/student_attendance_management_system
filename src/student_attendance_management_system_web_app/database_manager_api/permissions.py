from rest_framework.permissions import BasePermission, DjangoModelPermissions

from database_manager.models import Course


class DjangoModelPermissionsWithViewPermissionForGET(DjangoModelPermissions):
    """
    The request is authenticated using `django.contrib.auth` permissions.
    See: https://docs.djangoproject.com/en/dev/topics/auth/#permissions

    It ensures that the user is authenticated, and has the appropriate
    `view`/`add`/`change`/`delete` permissions on the model.

    This permission can only be applied against view classes that
    provide a `.queryset` attribute.
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class IsSuperUser(BasePermission):
    '''
    Allows access only to super users.
    '''
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class GivenCourseExists(BasePermission):
    '''
    Checks if a `Course` object with the same code as given in the URL argument exists.
    '''
    def has_permission(self, request, view):
        return Course.objects.filter(code=view.kwargs['code']).exists()


class IsStudentForGivenCourse(BasePermission):
    '''
    Allows access only to Students registered
    for the course whose code is passed as URL argument.
    '''
    def has_permission(self, request, view):
        return bool(
            request.user and
            hasattr(request.user, 'student') and
            Course.objects.filter(code=view.kwargs['code']).exists() and
            (request.user.student in Course.objects.get(code=view.kwargs['code']).registered_students.all())
        )


class IsInstructorForGivenCourse(BasePermission):
    '''
    Allows access only to Instructors registered as instructor
    for the course whose code is passed as URL argument.
    '''
    def has_permission(self, request, view):
        return bool(
            request.user and
            hasattr(request.user, 'classeventcoordinator') and
            hasattr(request.user.classeventcoordinator, 'instructor') and
            Course.objects.filter(code=view.kwargs['code']).exists() and
            (request.user.classeventcoordinator.instructor in Course.objects.get(code=view.kwargs['code']).instructors.all())
        )


class IsTeachingAssistantForGivenCourse(BasePermission):
    '''
    Allows access only to Teaching Assistants registered as teaching_assistant
    for the course whose code is passed as URL argument.
    '''
    def has_permission(self, request, view):
        return bool(
            request.user and
            hasattr(request.user, 'classeventcoordinator') and
            hasattr(request.user.classeventcoordinator, 'teachingassistant') and
            Course.objects.filter(code=view.kwargs['code']).exists() and
            (request.user.classeventcoordinator.teachingassistant in Course.objects.get(code=view.kwargs['code']).teaching_assistants.all())
        )
