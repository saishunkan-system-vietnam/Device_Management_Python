from django.shortcuts import render
from .models import Devices

def index(request):
    lstDevices = Devices.objects.filter(is_deleted=0)
    return render(request,'devices/index.html',{'data':lstDevices})