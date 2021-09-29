from django.urls import path, include
from . import views

from rest_framework import routers, serializers, viewsets
# from rest_framework.routers import DefaultRouter

# router = routers.DefaultRouter()
router = routers.DefaultRouter()
router.register('courses', views.CourseView)

urlpatterns = [
    path('', include(router.urls)),
]
