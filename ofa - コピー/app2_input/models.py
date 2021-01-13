from django.db import models
class EquipMeasurementTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_stop_date = models.DateTimeField()
    record_start_date = models.DateTimeField()
    record_stop_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    data_val = models.CharField(max_length=255)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'equip_measurement_tbl'
        get_latest_by = ['reg_date']

# Create your models here.
