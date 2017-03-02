import logging
from rest_framework import serializers
from annotations import models


logger = logging.getLogger(__package__)


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Record
        fields = '__all__'


class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Annotation
        fields = '__all__'

