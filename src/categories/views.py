from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


def categories(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    return HttpResponse("Hello, world. You're at the polls index.")
