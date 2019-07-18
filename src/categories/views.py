from django.shortcuts import render
from .models import Categories
from ..brands.models import brands
from .forms import CategoriesForm
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
import json


def index(request):
    categories = Categories.objects.filter(is_deleted=0)
    return render(request, 'categories/index.html', {'data': categories})


def add(request):
    lstBrands = brands.objects.filter(is_deleted=0).order_by('brand_name')

    brand_value_current = ''
    if request.POST.get('brands_id'):
        brand_value_current = int(request.POST.get('brands_id'))

    category_value_current = ''
    if request.POST.get('id_parent'):
        category_value_current = int(request.POST.get('id_parent'))

    if(request.method == 'POST'):
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category:index')
    else:
        form = CategoriesForm()
    return render(request, 'categories/add.html', {'form': form, 'lstBrands': lstBrands, 'brands_value_current': brand_value_current, 'category_value_current': category_value_current, 'is_parent_current': request.POST.get('is_parent')})


def edit(request, id=None):
    lstBrands = brands.objects.filter(is_deleted=0).order_by('brand_name')

    category = get_object_or_404(Categories, pk=id)

    brand_value_current = category.brands_id
    if request.POST.get('brands_id'):
        brand_value_current = int(request.POST.get('brands_id'))

    is_parent_current = ''
    if(category.id_parent == 0 or request.POST.get('is_parent')):
        is_parent_current = True

    category_value_current = category.id_parent
    if request.POST.get('id_parent'):
        category_value_current = int(request.POST.get('id_parent'))

    if(request.method == 'POST'):
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category:index')
    else:
        form = CategoriesForm(request.POST or None, instance=category)
    return render(request, 'categories/edit.html', {'form': form, 'id': category.id, 'lstBrands': lstBrands, 'brands_value_current': brand_value_current, 'category_value_current': category_value_current, 'is_parent_current': is_parent_current})


def get_category(request):
    brand_id = request.POST.get('brand_id')
    category_id = ''
    if request.POST.get('category_id'):
        category_id = int(request.POST.get('category_id'))
    lstCategory = Categories.objects.filter(is_deleted=0, brands_id=brand_id)
    options = '<option value="" hidden>---Select a category parent---</option>'
    if len(lstCategory) > 0:
        for item in lstCategory:
            options += '<option value="{0}" {1} >{2}</option>'.format(
                item.id, 'selected' if category_id == item.id else '', item.category_name)
    return HttpResponse(options)

def delete(request):
    if request.method == 'POST':
        data = Categories.objects.filter(id=request.POST.get('id')).update(is_deleted=1)
        if data == 1:
            return HttpResponse('1', request)
        else:
            return HttpResponse('2', request)
    else:
        return HttpResponse('2', request)
