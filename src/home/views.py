from django.shortcuts import render
from .form import product
from pprint import pprint

# Create your views here.
def home(request):   
    car = 'Không có session'  
    if 'my_car' in request.session : 
        car = request.session['my_car']
  
    return render(request, 'home.html', {'name' : car})

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