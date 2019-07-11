# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=150)

#     class Meta:
#         managed = False
#         db_table = 'auth_group'


# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)


# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)


# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'auth_user'


# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)


# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


# class BorrowDevices(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     borrower_id = models.IntegerField()
#     approved_id = models.IntegerField(blank=True, null=True)
#     handover_id = models.IntegerField(blank=True, null=True)
#     is_deleted = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'borrow_devices'


# class BorrowDevicesDetail(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     borrow_device_id = models.BigIntegerField()
#     device_id = models.BigIntegerField()
#     borrow_reason = models.TextField(blank=True, null=True)
#     return_reason = models.TextField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     borrow_date = models.DateTimeField()
#     approved_date = models.DateTimeField(blank=True, null=True)
#     return_date_expected = models.DateTimeField(blank=True, null=True)
#     return_date = models.DateTimeField()
#     created_user = models.CharField(max_length=100, blank=True, null=True)
#     update_user = models.CharField(max_length=100, blank=True, null=True)
#     created_time = models.DateTimeField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#     note_admin = models.TextField(blank=True, null=True)
#     is_deleted = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'borrow_devices_detail'


# class Brands(models.Model):
#     brand_name = models.CharField(max_length=100)
#     created_user = models.CharField(max_length=100, blank=True, null=True)
#     update_user = models.CharField(max_length=100, blank=True, null=True)
#     created_time = models.DateTimeField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#     is_deleted = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'brands'


# class Categories(models.Model):
#     id_parent = models.IntegerField(blank=True, null=True)
#     category_name = models.CharField(max_length=100)
#     created_user = models.CharField(max_length=100, blank=True, null=True)
#     update_user = models.CharField(max_length=100, blank=True, null=True)
#     created_time = models.DateTimeField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#     is_deleted = models.IntegerField()
#     brands_id = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'categories'


# class Devices(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     categories_id = models.IntegerField()
#     serial_number = models.CharField(max_length=50)
#     product_number = models.CharField(max_length=50)
#     name = models.CharField(max_length=100)
#     brand_id = models.IntegerField()
#     specifications = models.TextField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     purchase_date = models.DateTimeField(blank=True, null=True)
#     warranty_period = models.DateTimeField(blank=True, null=True)
#     created_user = models.CharField(max_length=100, blank=True, null=True)
#     update_user = models.CharField(max_length=100, blank=True, null=True)
#     created_time = models.DateTimeField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#     is_deleted = models.IntegerField()
#     image = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'devices'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.PositiveSmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)

#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'


# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)

#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)


# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_migrations'


# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'django_session'


# class Files(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     relate_id = models.BigIntegerField()
#     relate_name = models.CharField(max_length=50)
#     path = models.TextField()
#     type = models.CharField(max_length=50, blank=True, null=True)
#     created_user = models.CharField(max_length=100, blank=True, null=True)
#     update_user = models.CharField(max_length=100, blank=True, null=True)
#     created_time = models.DateTimeField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#     is_deleted = models.IntegerField()

#     class Meta:
#         managed = False
#         db_table = 'files'


# class Maintenances(models.Model):
#     devices_id = models.IntegerField()
#     status = models.IntegerField(blank=True, null=True)
#     broken_date = models.DateTimeField()
#     maintenance_start_date = models.DateTimeField(blank=True, null=True)
#     maintenances_end_date = models.DateTimeField(blank=True, null=True)
#     notificationer_broken = models.IntegerField()
#     create_user = models.CharField(max_length=100)
#     update_user = models.CharField(max_length=100, blank=True, null=True)
#     create_time = models.DateTimeField()
#     update_time = models.DateTimeField(blank=True, null=True)
#     is_deleted = models.IntegerField()
#     note = models.TextField(blank=True, null=True)
#     maintenances_address = models.TextField(blank=True, null=True)
#     total_payment = models.BigIntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'maintenances'


# class Test(models.Model):
#     dd = models.DateTimeField()

#     class Meta:
#         managed = False
#         db_table = 'test'


# class Users(models.Model):
#     user_name = models.CharField(max_length=100)
#     full_name = models.CharField(max_length=255)
#     position = models.CharField(max_length=100)
#     level = models.IntegerField(blank=True, null=True)
#     created_user = models.CharField(max_length=100, blank=True, null=True)
#     update_user = models.CharField(max_length=100, blank=True, null=True)
#     created_time = models.DateTimeField(blank=True, null=True)
#     update_time = models.DateTimeField(blank=True, null=True)
#     is_deleted = models.IntegerField()
#     email = models.CharField(max_length=100)
#     team = models.CharField(max_length=100, blank=True, null=True)
#     address = models.CharField(max_length=250, blank=True, null=True)
#     birthdate = models.DateField(blank=True, null=True)
#     join_date = models.DateField(blank=True, null=True)
#     status = models.IntegerField(blank=True, null=True)
#     img = models.CharField(max_length=250, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'users'
