from django.urls import path, include
from rest_framework import routers

from .views import AnagramAPIView, DevicesAPIViewSet, EndpointsAPIViewSet, TestTaskView, devices_query_api_view

router = routers.DefaultRouter()
router.register(r'devices', DevicesAPIViewSet)
router.register(r'endpoints', EndpointsAPIViewSet)

urlpatterns = [
    path('', TestTaskView.as_view()),
    path('anagram/', AnagramAPIView.as_view()),
    path('devices_query/', devices_query_api_view)
]
urlpatterns += router.urls
