from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated

from permissions import *

from .models import Department

from .serializer import *

class FacultyAPIListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = Department.objects.all()
    serializer_class = FacultySerializer

class FacultyAPIDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsITAdmin]
    queryset = Department.objects.all()
    serializer_class = FacultySerializer