import logging
from rest_framework.viewsets import ModelViewSet
from annotations import models
from annotations import serializers
from django.http import JsonResponse

logger = logging.getLogger(__package__)


class RecordViewSet(ModelViewSet):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer 


class AnnotationViewSet(ModelViewSet):
    queryset = models.Annotation.objects.all()
    serializer_class = serializers.AnnotationSerializer


    def delete(self, request):
    	x1 = request.data['x1']
    	x2 = request.data['x2']
    	t1 = request.data['t1']
    	t2 = request.data['t2']
    	record = request.data['record']
    	models.Annotation.objects.get(x1=x1, x2=x2, t1=t1, t2=t2, record=record).delete()
    	return JsonResponse({})