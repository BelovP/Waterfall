from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from annotations import api as annotations_api
from annotations import views as annotations_views

admin.site.site_header = 'Waterfall'


# API
api_router = routers.DefaultRouter()
api_router.register(r'records', annotations_api.RecordViewSet)
api_router.register(r'annotations', annotations_api.AnnotationViewSet)


urlpatterns = [
    url(r'^', annotations_views.SpaView.as_view()),
    url(r'^api/v1/', include(api_router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]


