from django.db import models

class brands(models.Model):
    brand_name = models.CharField(max_length=100)
    created_user = models.CharField(max_length=100, blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(default = 0)
    class Meta:
        managed = False
        db_table = 'brands'
