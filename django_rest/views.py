from rest_framework import viewsets
from django_rest import models, serializers


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = serializers.ManufacturerSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ShoeType.objects.all()
    serializer_class = serializers.ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    queryset = models.ShoeColor.objects.all()
    serializer_class = serializers.ShoeColorSerializer
