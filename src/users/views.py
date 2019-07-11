from django.shortcuts import render
from .models import Users
# Create your views here.


def user(request):
    title = "List users"
    all_objects = Users.objects.all()
    context = {'all_objects': all_objects}
    # for x in context['all_objects']:
    #     print(x)
    return render(request, 'index.html', {'title': title, 'context': context['all_objects']})
