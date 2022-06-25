from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))

CONTENT = []
with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
    file_reader = csv.reader(file, delimiter=",")
    count = 0
    for row in file_reader:
        if count != 0:
            data = (
                row[1],
                row[4],
                row[6]
            )
            CONTENT.append(data)
        count += 1

def bus_stations(request):

    page_number = int(request.GET.get('page',1))
    paginator = Paginator(CONTENT, 15)
    page = paginator.get_page(page_number)
    context = {
        'page': page,
    }

    return render(request, 'stations/index.html', context)
