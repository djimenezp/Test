# Create your views here.
from rest_framework.viewsets import ModelViewSet

from app import models, serializers


class ItemViewSet(ModelViewSet):
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


class ColorViewSet(ModelViewSet):
    queryset = models.Color.objects.all()
    serializer_class = serializers.ColorSerializer


class StatusViewSet(ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
