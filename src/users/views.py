from django.shortcuts import render
import logging
from .models import Users
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .form import UserForm
from django.contrib import messages

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
        u = Users.objects.get(id=id)
        if form.is_valid():
            u.user_name = request.POST['user_name']
            u.full_name = request.POST['full_name']
            u.email = request.POST['email']
            u.birthdate = request.POST['dateofbirth']
            u.address = request.POST['address']
            u.join_date = request.POST['joindate']
            try:
                u.save()
                messages.success(request, 'Update user %s success!' % request.POST['user_name'])
                logging.getLogger("info_logger").info('Save data User id = %s success' % id)
                return HttpResponseRedirect(reverse('user'))
            except Exception as e:
                messages.error(request, e)
                logging.getLogger("error_logger").info(repr(e))
                pass
                return render(request, 'edit.html', {'title': title, 'user': u})
        else:
            user = Users.objects.get(pk=id)
            messages.error(request, 'Something went wrong!')
            # return HttpResponseRedirect(reverse('user'))
            return render(request, 'edit.html', {'title': title, 'user': user})


# def update(request, id):print(request)
#     if request.method == 'POST':
#         print(request)
#     else:
#         return render(request, 'edit.html', {'title': title})
