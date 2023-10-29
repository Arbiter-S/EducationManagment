from .models import *
from .serializer import *
from rest_framework.generics import *

class EducationalAssistantAPIListCreateView(ListCreateAPIView):
    queryset = EducationalAssistant.objects.all()
    serializer_class = EducationalAssistantSerializer
    
class EducationalAssistantAPIDetailView(RetrieveUpdateDestroyAPIView):
    queryset = EducationalAssistant.objects.all()
    serializer_class = EducationalAssistantSerializer
