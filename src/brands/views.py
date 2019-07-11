from django.shortcuts import render

# Create your views here.

def brand(request):     
    from .models import brands
    data= brands.objects.all()   
    return render(request, 'brand.html', {'data': data})
