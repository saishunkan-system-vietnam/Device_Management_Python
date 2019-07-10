from django.shortcuts import render
import logging

# Create your views here.
def home(request):
    logging.getLogger("error_logger").error("Hi I am here");
    logging.getLogger("info_logger").info("Hi I am here info");
    return render(request, 'home.html')

def addproduct(request):
    return render(request, 'addproduct.html')