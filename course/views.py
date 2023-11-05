from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, CreateAPIView

from .models import *
from .serializers import *


class ApprovedCourseViewSet(viewsets.ModelViewSet):
    queryset = ApprovedCourse.objects.all()
    serializer_class = ApprovedCoueseSerializer


class SemesterCourseAPICreateView(CreateAPIView):
    queryset = SemesterCourse.objects.all()
    serializer_class = SemesterCourseSerializer