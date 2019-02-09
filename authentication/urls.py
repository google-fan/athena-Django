from rest_framework import routers

from .views import UserViewSet, GroupViewSet, StudentViewSet, TutorViewSet, TeacherViewSet

auth_router = routers.DefaultRouter()
auth_router.register('users', UserViewSet)
auth_router.register('groups', GroupViewSet)
auth_router.register('students', StudentViewSet)
auth_router.register('tutors', TutorViewSet)
auth_router.register('teachers', TeacherViewSet)
