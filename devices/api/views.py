from rest_framework import viewsets, views
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from django.db import connection

from .serializers import AnagramSerializer, DevicesSerializer, EndpointsSerializer
from .models import Devices, Endpoints


class AnagramAPIView(GenericAPIView):
    serializer_class = AnagramSerializer

    def get(self, *args, **kwargs):
        return Response({'message': 'Введите две строки'})

    def post(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data)


class DevicesAPIViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=HTTP_201_CREATED)


class EndpointsAPIViewSet(viewsets.ModelViewSet):
    queryset = Endpoints.objects.all()
    serializer_class = EndpointsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=HTTP_201_CREATED)


@api_view(['GET', ])
def devices_query_api_view(request, *args, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute(
            'select devices.dev_type, count(*) from devices left join endpoints '
            'on devices.id = endpoints.device_id where endpoints.device_id is null '
            'group by devices.dev_type;'
        )
        data = {k: v for k, v in cursor.fetchall()}
    return Response(data)


class TestTaskView(views.APIView):

    def get(self, request, *args, **kwargs):
        apidocs = {
            'anagram': request.build_absolute_uri('anagram/'),
            'devices': request.build_absolute_uri('devices/'),
            'endpoints': request.build_absolute_uri('endpoints/'),
            'devices_query': request.build_absolute_uri('devices_query/'),
        }
        return Response(apidocs)
