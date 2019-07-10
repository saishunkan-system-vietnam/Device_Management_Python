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