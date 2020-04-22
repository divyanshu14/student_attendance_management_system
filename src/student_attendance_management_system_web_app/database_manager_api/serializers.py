from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from database_manager.models import (
    Student,
    ClassEventCoordinator,
    Instructor,
    TeachingAssistant,
    Course,
    ClassEvent,
)


DEFAULT_PASSWORD = "new_pass_123"


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("Email address"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(validated_data['email'],
                                                    DEFAULT_PASSWORD
                                                    )
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance


class StudentUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('user', 'entry_number',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(validated_data=user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student

    def update(self, instance, validated_data):
        user_data = validated_data.get('user')
        if user_data != None:
            validated_data.pop('user')
            UserSerializer().update(instance=instance.user, validated_data=user_data)
        instance.entry_number = validated_data.get('entry_number', instance.entry_number)
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    # If we don't specify this, API will expect primary key instead of email thereby raising
    # "Incorrect type. Expected pk value, received str." if we provide email.
    user = serializers.SlugRelatedField(slug_field='email', queryset=get_user_model().objects.filter(student__isnull=True))

    class Meta:
        model = Student
        fields = ('user', 'entry_number',)


class ClassEventCoordinatorUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ClassEventCoordinator
        fields = ('user',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer().create(validated_data=user_data)
        class_event_coordinator = ClassEventCoordinator.objects.create(user=user, **validated_data)
        return class_event_coordinator

    def update(self, instance, validated_data):
        user_data = validated_data.get('user')
        if user_data != None:
            validated_data.pop('user')
            UserSerializer().update(instance=instance.user, validated_data=user_data)
        return instance


class ClassEventCoordinatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassEventCoordinator
        fields = ('user',)

    def create(self, validated_data):
        if hasattr(validated_data['user'], 'classeventcoordinator'):
            return validated_data['user'].classeventcoordinator
        class_event_coordinator = ClassEventCoordinator.objects.create(user=validated_data['user'])
        return class_event_coordinator


class ClassEventCoordinatorNotInstructorSerializer(ClassEventCoordinatorSerializer):
    # If we don't specify this, API will expect primary key instead of email thereby raising
    # "Incorrect type. Expected pk value, received str." if we provide email.
    user = serializers.SlugRelatedField(slug_field='email', queryset=get_user_model().objects.filter(classeventcoordinator__instructor__isnull=True))


class ClassEventCoordinatorNotTeachingAssistantSerializer(ClassEventCoordinatorSerializer):
    # If we don't specify this, API will expect primary key instead of email thereby raising
    # "Incorrect type. Expected pk value, received str." if we provide email.
    user = serializers.SlugRelatedField(slug_field='email', queryset=get_user_model().objects.filter(classeventcoordinator__teachingassistant__isnull=True))


class InstructorClassEventCoordinatorUserSerializer(serializers.ModelSerializer):
    class_event_coordinator = ClassEventCoordinatorUserSerializer()

    class Meta:
        model = Instructor
        fields = ('class_event_coordinator', 'instructor_id',)

    def create(self, validated_data):
        class_event_coordinator_user_data = validated_data.pop('class_event_coordinator')
        class_event_coordinator = ClassEventCoordinatorUserSerializer().create(validated_data=class_event_coordinator_user_data)
        instructor = Instructor.objects.create(class_event_coordinator=class_event_coordinator, **validated_data)
        return instructor

    def update(self, instance, validated_data):
        class_event_coordinator_user_data = validated_data.get('class_event_coordinator')
        if class_event_coordinator_user_data != None:
            validated_data.pop('class_event_coordinator')
            ClassEventCoordinatorUserSerializer().update(instance=instance.class_event_coordinator, validated_data=class_event_coordinator_user_data)
        instance.instructor_id = validated_data.get('instructor_id', instance.instructor_id)
        instance.save()
        return instance


class InstructorSerializer(serializers.ModelSerializer):
    class_event_coordinator = ClassEventCoordinatorNotInstructorSerializer()

    class Meta:
        model = Instructor
        fields = ('class_event_coordinator', 'instructor_id',)

    def create(self, validated_data):
        class_event_coordinator_data = validated_data.pop('class_event_coordinator')
        class_event_coordinator = ClassEventCoordinatorNotInstructorSerializer().create(validated_data=class_event_coordinator_data)
        instructor = Instructor.objects.create(class_event_coordinator=class_event_coordinator, **validated_data)
        return instructor


class TeachingAssistantClassEventCoordinatorUserSerializer(serializers.ModelSerializer):
    class_event_coordinator = ClassEventCoordinatorUserSerializer()

    class Meta:
        model = TeachingAssistant
        fields = ('class_event_coordinator', 'teaching_assistant_id',)

    def create(self, validated_data):
        class_event_coordinator_user_data = validated_data.pop('class_event_coordinator')
        class_event_coordinator = ClassEventCoordinatorUserSerializer().create(validated_data=class_event_coordinator_user_data)
        teaching_assistant = TeachingAssistant.objects.create(class_event_coordinator=class_event_coordinator, **validated_data)
        return teaching_assistant

    def update(self, instance, validated_data):
        class_event_coordinator_user_data = validated_data.get('class_event_coordinator')
        if class_event_coordinator_user_data != None:
            validated_data.pop('class_event_coordinator')
            ClassEventCoordinatorUserSerializer().update(instance=instance.class_event_coordinator, validated_data=class_event_coordinator_user_data)
        instance.teaching_assistant_id = validated_data.get('teaching_assistant_id', instance.teaching_assistant_id)
        instance.save()
        return instance


class TeachingAssistantSerializer(serializers.ModelSerializer):
    class_event_coordinator = ClassEventCoordinatorNotTeachingAssistantSerializer()

    class Meta:
        model = TeachingAssistant
        fields = ('class_event_coordinator', 'teaching_assistant_id',)

    def create(self, validated_data):
        class_event_coordinator_data = validated_data.pop('class_event_coordinator')
        class_event_coordinator = ClassEventCoordinatorNotTeachingAssistantSerializer().create(validated_data=class_event_coordinator_data)
        teaching_assistant = TeachingAssistant.objects.create(class_event_coordinator=class_event_coordinator, **validated_data)
        return teaching_assistant


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'name',
            'code',
            'relative_attendance_for_one_lecture',
            'relative_attendance_for_one_tutorial',
            'relative_attendance_for_one_practical',
            'instructors',
            'teaching_assistants',
            'registered_students',
        )


class CurrentClassEventCoordinatorDefault:
    '''
    Represents the `ClassEventCoordinator` object related to the current authenticated user.
    Make sure that the logged in User has related classeventcoordinator property before
    using this class as a default, otherwise
    `database_manager.models.User.classeventcoordinator.RelatedObjectDoesNotExist` will be raised.
    '''
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context['request'].user.classeventcoordinator

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class CurrentCourseDefault:
    '''
    Represents the `Course` object with code `code` as passed in the URL keyword argument.
    Make sure that the `code` passed in the URL keyword argument is a valid one before
    using this class as a default, otherwise `database_manager.models.Course.DoesNotExist`
    will be raised.
    '''
    requires_context = True

    def __call__(self, serializer_field):
        return Course.objects.get(code=serializer_field.context['view'].kwargs['code'])

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class ClassEventSerializer(serializers.ModelSerializer):
    course = serializers.HiddenField(default=CurrentCourseDefault())
    attendance_taken_by = ClassEventCoordinatorUserSerializer(default=CurrentClassEventCoordinatorDefault(), read_only=True)
    present_students = StudentUserSerializer(many=True, read_only=True)

    class Meta:
        model = ClassEvent
        fields = (
            'course',
            'timestamp',
            'class_event_type',
            'attendance_taken_by',
            'present_students',
        )
