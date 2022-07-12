from django.urls import path

from measurement.views import SensorListView, OneSensorView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensor/<pk>/', OneSensorView.as_view()),
]
