from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {'phones': Phone.objects.all()}
    sorting_get = request.GET.get('sort')
    sorting = {
        'name':'name',
        'min_price':'price',
        'max_price':'-price'
    }
    if sorting_get:
        context={'phones':Phone.objects.all().order_by(sorting[sorting_get])}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone':Phone.objects.filter(slug=slug).first()}
    return render(request, template, context)
