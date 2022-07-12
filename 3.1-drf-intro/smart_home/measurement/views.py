# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
import datetime

from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        return serializer.save()


class OneSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def perform_create(self, serializer):
        return serializer.save(date=datetime.datetime.now())
