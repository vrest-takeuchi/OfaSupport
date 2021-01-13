from django.db import models
class AnaSummary(models.Model):
    equip_id = models.BigIntegerField()
    run_start_date = models.DateTimeField()
    result = models.CharField(max_length=100)
    block_no = models.BigIntegerField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    sub_category = models.CharField(max_length=100, blank=True, null=True)
    offpoint_category = models.CharField(max_length=100, blank=True, null=True)
    offpoint = models.BigIntegerField(blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    measurement_base_time = models.DateTimeField(blank=True, null=True)
    evaluation_place = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ana_summary'

# Create your models here.
