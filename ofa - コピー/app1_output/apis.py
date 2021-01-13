from rest_framework import viewsets, routers
from app1_output.models import AnaSummary
from app1_output.serializers import AnaSummarySerializer

class AnaSummaryViewSet(viewsets.ModelViewSet):
    queryset = AnaSummary.objects.all()
    serializer_class = AnaSummarySerializer

router = routers.DefaultRouter()
router.register(r'articles', AnaSummaryViewSet)