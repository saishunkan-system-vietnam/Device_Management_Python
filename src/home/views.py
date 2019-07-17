from django.shortcuts import render, redirect
from .form import product
from pprint import pprint
import logging

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    try:
        #raise Exception("Custom error thrown by newbie developer :D")
        logging.getLogger("info_logger").info(request);
        return render(request, 'home.html')
    except Exception as e:
        logging.getLogger("error_logger").error(repr(e))
        pass

def addproduct(request):
    stringname = ""
    if(request.method == 'POST'):
        form= product(request.POST)
        stringname = request.POST.get("subject")
        if 'my_car' in request.session:
            request.session.pop('my_car')
        else:
            request.session['my_car']= 'oto'
    else:
        form= product()

    return render(request, 'addproduct.html', {'form' : form})
