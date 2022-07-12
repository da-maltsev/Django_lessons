from django.urls import path

from measurement.views import SensorListView, OneSensorView, MeasurementCreateView

urlpatterns = [
    path('sensor/', SensorListView.as_view()),
    path('sensor/<pk>/', OneSensorView.as_view()),
    path('measurement/', MeasurementCreateView.as_view()),
]
