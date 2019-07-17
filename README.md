# Project for learning Python and Django framework for WINDOWS

## InFo
1. Python 3.7.4
2. Django 2.2.3
3. MySql
4. Pip 19.0.3

## Document
1. Django framework: https://docs.djangoproject.com/en/2.2/
2. install Pip: https://pip.pypa.io/en/stable/installing/
3. install python: https://www.python.org/downloads/windows/

## How to run app
1. install pip
2. install Python
3. install django (run in CLI): pip install django
4. run(CLI):pip install pymysql
            pip install mysqlclient
5. run CLI in root folder: python manage.py runserver (run project)
6. create new app (run inside src folder): python ../manage.py startapp <module name>

## Use log
1. Add in view.py
```
    import logging
```
2. Then to get something out do this
```
    logging.getLogger("error_logger").error("Error log");
    logging.getLogger("info_logger").info("Info log");
```

## Use Django ORM
1. Auto-generate the models
```
    python manage.py inspectdb > models.py
    or for table: python manage.py inspectdb TableName > output.py
```
Document: https://docs.djangoproject.com/en/2.2/howto/legacy-databases/

2. In model.py with table name: (example model User)
```
    class Users(models.Model):
    user_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    level = models.IntegerField(blank=True, null=True)
    created_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    email = models.CharField(max_length=100)
    team = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
```

3. In views.py File
```
    from django.shortcuts import render
    from .models import Users
    # Create your views here.


    def user(request):
        title = "List users"
        all_objects = Users.objects.all()
        context = {'all_objects': all_objects}
        print(context)
        return render(request, 'index.html', {'title': title, 'context': context})
```

## Condition in where:
https://docs.djangoproject.com/en/2.2/topics/db/queries/
https://docs.djangoproject.com/en/2.2/topics/db/queries/
```
    brands.objects.filter(is_deleted=0, id = 2)
    id__gte = 2 <=> id >=2
    id__gt = 2  <=> id >2
    id__lte = 2 <=> id <=2
    id__lt = 2  <=> id <2

    Entry.objects.all().filter(pub_date__year=2006)
    pub_date__year=2006 <=> year(pub_date)=2006
```

## How to create django class from exist table
1. You can auto generate models with:
```
    python manage.py inspectdb
```

2. in order to save the output to a file
```
    python manage.py inspectdb > models_from_db.py
```

3. You can get generate for just one table passing the table name to the command
```
    python manage.py inspectdb table > models_from_db.py
```

Read mode auto generate models: https://docs.djangoproject.com/en/2.1/howto/legacy-databases/#auto-generate-the-models
Read mode inspectdb: https://docs.djangoproject.com/en/2.1/ref/django-admin/#django-admin-inspectdb
