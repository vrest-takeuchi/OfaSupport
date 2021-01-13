from django.db import models

class AccelerationTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_end_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    nine_axis_acceleration_x = models.CharField(max_length=20)
    nine_axis_acceleration_y = models.CharField(max_length=20)
    nine_axis_acceleration_z = models.CharField(max_length=20)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'acceleration_tbl'


class AngularvelocityTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_end_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    nine_axis_angular_velocity_x = models.CharField(max_length=20)
    nine_axis_angular_velocity_y = models.CharField(max_length=20)
    nine_axis_angular_velocity_z = models.CharField(max_length=20)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'angularvelocity_tbl'


class CanAccelTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_end_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    can_accel = models.CharField(max_length=20)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'can_accel_tbl'


class CanBrakeTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_end_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    can_brake = models.CharField(max_length=20)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'can_brake_tbl'


class CanPositionTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_end_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    can_turn_lever_position = models.CharField(max_length=20)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'can_position_tbl'


class CanSpeedTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_end_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    can_speed = models.CharField(max_length=20)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'can_speed_tbl'


class CanSteeringTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_end_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    can_steering = models.CharField(max_length=20)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'can_steering_tbl'


class EquipStatusTbl(models.Model):
    equip_id = models.BigIntegerField(primary_key=True)
    startup_st = models.TextField()  # This field type is a guess.
    operation_st = models.TextField()  # This field type is a guess.
    mqtt_st = models.TextField()  # This field type is a guess.
    device_st = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'equip_status_tbl'


class GeomagnetismTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_end_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    nine_axis_geomagnetism_x = models.CharField(max_length=20)
    nine_axis_geomagnetism_y = models.CharField(max_length=20)
    nine_axis_geomagnetism_z = models.CharField(max_length=20)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'geomagnetism_tbl'


class LocationTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_end_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    gps_date = models.CharField(max_length=20)
    latitude = models.CharField(max_length=20)
    latitude_direction = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    longitude_direction = models.CharField(max_length=20)
    velocity = models.CharField(max_length=20)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'location_tbl'


class SatelliteTbl(models.Model):
    id = models.BigAutoField(primary_key=True)
    equip_id = models.BigIntegerField()
    device_id = models.BigIntegerField()
    seqno = models.BigIntegerField()
    measurement_date = models.DateTimeField()
    run_start_date = models.DateTimeField()
    run_end_date = models.DateTimeField()
    type_id = models.BigIntegerField()
    positioning_quality = models.CharField(max_length=20)
    used_satellites = models.CharField(max_length=20)
    reg_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'satellite_tbl'


# Create your models here.
