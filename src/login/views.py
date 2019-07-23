from django.shortcuts import render
import configs.contants as contants
# import requests
import json
from ..users.models import Users
from django.contrib.auth import authenticate, login


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        url = contants.URL_LOGIN + request.POST['username'] + '&passwd=' + request.POST['password'] + '&session=Chat&format=cookie'
        headers = {'content-type': 'application/json'}
        result = requests.get(url, headers=headers).text
        data = json.loads(result)
        if data and data['success'] == True:
            data_user = Users.objects.filter(user_name=request.POST['username'], status=0)
            print(data['success'])
        return render(request, 'login.html')


# Create your views here.
