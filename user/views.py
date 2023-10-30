from rest_framework.generics import *

from .models import *

from .serializer import *



class ProfessorAPIListView(ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ProfessorAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class EducationalAssistantAPIListView(ListCreateAPIView):
    queryset = EducationalAssistant.objects.all()
    serializer_class = EducationalAssistantSerializer
    
class EducationalAssistantAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = EducationalAssistant.objects.all()
    serializer_class = EducationalAssistantSerializer
