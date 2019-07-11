from django.db import models

# Create your models here.


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
