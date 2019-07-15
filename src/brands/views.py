from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import brands
from django.urls import reverse
from .form import BrandForm


def brand(request):
    data = brands.objects.filter(is_deleted=0)
    return render(request, 'brand.html', {'data': data})


def add_brand(request):

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('brand:index'))
        else:
            print("Lỗi")
    else:
        form = BrandForm()
   
    return render(request, 'add_brand.html', {"form": form})


# def edit_brand(request):
#     brand_name="";
#     if request.method == 'POST':
#         brand_name = request.POST['brand_name']
#         if (brand_name != ''):
#             brand_new = brands(brand_name = brand_name)
#             result = brand_new.save()
#             return HttpResponseRedirect(reverse('brand'))
#     return render(request, 'add_brand.html', {"brand_name": brand_name})
