from rest_framework.generics import *

from .models import *
from .serializers import *


class TermAPIListView(ListCreateAPIView):
    queryset = Term.objects.all()
    serializer_class = TermSerializer


class TermAPIDetailView(RetrieveUpdateAPIView):
    queryset = Term.objects.all()
    serializer_class = TermSerializer
