from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from .models import brands
from django.urls import reverse
from .form import BrandForm
from django.db.models.functions import TruncMonth
from django.db.models import Count


def brand(request):
    data = brands.objects.filter(is_deleted=0).order_by('brand_name')
    return render(request, 'brands/index.html', {'data': data})


def add(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('brand:index'))
    else:
        form = BrandForm()
    return render(request, 'brands/add.html', {"form": form})


def edit(request, id=None):
    brand = get_object_or_404(brands, id=id)
    form = BrandForm(request.POST or None, instance=brand)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('brand:index'))
    return render(request, 'brands/edit.html',  {"form": form, 'id': id})


def delete(request):
    if request.method == 'POST':
        data = brands.objects.filter(
            id=request.POST.get('id')).update(is_deleted=1)
        if data == 1:
            return HttpResponse('1', request)
        else:
            return HttpResponse('2', request)
    else:
        return HttpResponse('2', request)


def chart(request):

    data = brands.objects.raw(
        'SELECT COUNT(id) as quantity, MONTH(created_time) as created_month FROM brands GROUP BY MONTH(created_time)')
    print(data)
    return render(request, 'brands/chart.html')
