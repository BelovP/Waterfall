import logging
from django.db import models


logger = logging.getLogger(__package__)


class Record(models.Model):
    """
    Binary file recorded from the device

    TODO: more realistic model required
    """
    filename = models.CharField(max_length=255)


class Annotation(models.Model):
    """
    Rectangular time-space annotation on the waterfall. 

    Time in seconds, x in meters 
    """
    record = models.ForeignKey(Record, related_name='annotations', verbose_name='Record')
    t1 = models.FloatField()
    t2 = models.FloatField()
    x1 = models.FloatField()
    x2 = models.FloatField()
    label = models.CharField(max_length=255, null=True, blank=True)
