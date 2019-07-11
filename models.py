# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BorrowDevices(models.Model):
    id = models.BigAutoField(primary_key=True)
    borrower_id = models.IntegerField()
    approved_id = models.IntegerField(blank=True, null=True)
    handover_id = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'borrow_devices'


class BorrowDevicesDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    borrow_device_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    borrow_reason = models.TextField(blank=True, null=True)
    return_reason = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    borrow_date = models.DateTimeField()
    approved_date = models.DateTimeField(blank=True, null=True)
    return_date_expected = models.DateTimeField(blank=True, null=True)
    return_date = models.DateTimeField()
    created_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    note_admin = models.TextField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'borrow_devices_detail'


class Brands(models.Model):
    brand_name = models.CharField(max_length=100)
    created_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'brands'


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


class Files(models.Model):
    id = models.BigAutoField(primary_key=True)
    relate_id = models.BigIntegerField()
    relate_name = models.CharField(max_length=50)
    path = models.TextField()
    type = models.CharField(max_length=50, blank=True, null=True)
    created_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'files'


class Maintenances(models.Model):
    devices_id = models.IntegerField()
    status = models.IntegerField(blank=True, null=True)
    broken_date = models.DateTimeField()
    maintenance_start_date = models.DateTimeField(blank=True, null=True)
    maintenances_end_date = models.DateTimeField(blank=True, null=True)
    notificationer_broken = models.IntegerField()
    create_user = models.CharField(max_length=100)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    maintenances_address = models.TextField(blank=True, null=True)
    total_payment = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenances'


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
