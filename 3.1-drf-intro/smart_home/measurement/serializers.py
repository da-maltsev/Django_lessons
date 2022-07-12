from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'date']

class MeasurementSerializerSens(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializerSens(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'title', 'description', 'measurements']