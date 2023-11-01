from rest_framework.generics import *
from .models import Department
from .serializer import *

class FacultyAPIListView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = FacultySerializer

class FacultyAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = FacultySerializer