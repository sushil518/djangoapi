# from rest_framework import serializers
from rest_framework import routers, serializers, viewsets
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'url', 'name', 'language', 'price']
