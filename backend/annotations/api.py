import logging
from rest_framework.viewsets import ModelViewSet
from annotations import models
from annotations import serializers


logger = logging.getLogger(__package__)


class RecordViewSet(ModelViewSet):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer


class AnnotationViewSet(ModelViewSet):
    queryset = models.Annotation.objects.all()
    serializer_class = serializers.AnnotationSerializer






