from django.shortcuts import render
import logging

# Create your views here.
def home(request):
    try:
        #raise Exception("Custom error thrown by newbie developer :D")
        logging.getLogger("info_logger").info(request);
        return render(request, 'home.html')
    except Exception as e:
        logging.getLogger("error_logger").error(repr(e))
        pass

def addproduct(request):
    return render(request, 'addproduct.html')