from django.contrib import admin
from annotations import models


class AnnotationAdmin(admin.ModelAdmin):
    list_display    = ('id', 
                       'record',
                       'label',
                       't1',
                       't2',
                       'x1',
                       'x2',)  


admin.site.register(models.Record)
admin.site.register(models.Annotation, AnnotationAdmin)
