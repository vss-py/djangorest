from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristicos
from .serializers import PontosTuristicosSerializer

class PontosTuristicosViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = PontosTuristicos.objects.all()
    serializer_class = PontosTuristicosSerializer