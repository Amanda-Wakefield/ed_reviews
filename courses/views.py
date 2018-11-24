from rest_framework import generics

from . import models
from . import serializers


class ListCreateCourseView(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class RetrieveUpdateDestroyCourseView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
