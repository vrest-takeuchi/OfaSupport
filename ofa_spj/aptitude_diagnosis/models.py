from django.db import models
class Score1(models.Model):
    summary_id = models.BigIntegerField(blank=True, null=True)
    summary_category_id = models.BigIntegerField(blank=True, null=True)
    score_category = models.BigIntegerField(blank=True, null=True)
    point = models.BigIntegerField(blank=True, null=True)
    point_rank = models.CharField(max_length=20, blank=True, null=True)
    average = models.BigIntegerField(blank=True, null=True)
    deviation = models.BigIntegerField(blank=True, null=True)
    rank_office = models.BigIntegerField(blank=True, null=True)
    num_office = models.BigIntegerField(blank=True, null=True)
    rank_area = models.BigIntegerField(blank=True, null=True)
    num_area = models.BigIntegerField(blank=True, null=True)
    office_id = models.BigIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'score1'


class Summary1(models.Model):
    car_id = models.BigIntegerField(blank=True, null=True)
    run_start_date = models.TimeField(blank=True, null=True)
    total_score = models.CharField(max_length=20, blank=True, null=True)
    total_score_rank = models.CharField(max_length=20, blank=True, null=True)
    mental_score = models.CharField(max_length=20, blank=True, null=True)
    tech_score = models.CharField(max_length=20, blank=True, null=True)
    physical_score = models.CharField(max_length=20, blank=True, null=True)
    total_comment = models.TextField(blank=True, null=True)
    mental_comment = models.TextField(blank=True, null=True)
    mental_required_training_comment = models.TextField(blank=True, null=True)
    mental_training_comment = models.TextField(blank=True, null=True)
    tech_comment = models.TextField(blank=True, null=True)
    tech_required_training_comment = models.TextField(blank=True, null=True)
    tech_training_comment = models.TextField(blank=True, null=True)
    physical_comment = models.TextField(blank=True, null=True)
    physical_required_training_comment = models.TextField(blank=True, null=True)
    physical_training_comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summary1'




class Training1(models.Model):
    score_id = models.BigIntegerField(blank=True, null=True)
    training_id = models.BigIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'training1'


# Create your models here.
