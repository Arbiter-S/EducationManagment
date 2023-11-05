from rest_framework import viewsets
from .models import ApprovedCourse
from .serializers import ApprovedCourseSerializer


class ApprovedCourseViewSet(viewsets.ModelViewSet):
    queryset = ApprovedCourse.objects.all()
    serializer_class = ApprovedCourseSerializer
