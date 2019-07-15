from django.shortcuts import render
from .models import Users
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .form import UserForm
import logging

#from django.forms import

# Create your views here.

title = "List users"
def user(request):
    all_objects = Users.objects.all()
    context = {'all_objects': all_objects}
    return render(request, 'index.html', {'title': title, 'context': context['all_objects']})

def edit(request, id):
    title = "Edit user profile"
    if request.method == 'GET':
        try:
            user = Users.objects.get(pk=id)
        except Users.DoesNotExist:
            raise Http404("User does not exist")
        return render(request, 'edit.html', {'title': title, 'user': user})
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = Users.objects.get(id = id)
            u.user_name = request.POST['user_name']
            u.full_name = request.POST['full_name']
            u.email = request.POST['email']
            u.birthdate = request.POST['dateofbirth']
            u.address = request.POST['address']
            u.join_date = request.POST['joindate']
            u.save()
            user = Users.objects.get(pk=id)
            logging.getLogger("info_logger").info("Save data User success")
            return HttpResponseRedirect(reverse('user'), {'errors': 'Save data User success'})
        else:
            user = Users.objects.get(pk=id)
            # return HttpResponseRedirect(reverse('user'))
            return render(request, 'edit.html', {'title': title, 'user': user, 'errors': form.non_field_errors()})


# def update(request, id):print(request)
#     if request.method == 'POST':
#         print(request)
#     else:
#         return render(request, 'edit.html', {'title': title})
