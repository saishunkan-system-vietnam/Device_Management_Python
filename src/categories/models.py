from django.db import models

# Create your models here.


class Categories(models.Model):
    id_parent = models.IntegerField(blank=True, null=True)
    category_name = models.CharField(max_length=100)
    created_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    brands_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'categories'
