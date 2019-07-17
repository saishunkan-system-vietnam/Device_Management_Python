# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Devices(models.Model):
    id = models.BigAutoField(primary_key=True)
    categories_id = models.IntegerField()
    serial_number = models.CharField(max_length=50)
    product_number = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    brand_id = models.IntegerField()
    specifications = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    purchase_date = models.DateTimeField(blank=True, null=True)
    warranty_period = models.DateTimeField(blank=True, null=True)
    created_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devices'
