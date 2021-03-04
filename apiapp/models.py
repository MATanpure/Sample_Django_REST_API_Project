from django.db import models

# Create your models here.


class Member(models.Model):

    """Model- Member"""

    id = models.CharField(max_length=50, primary_key=True)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=100)

    class Meta:
        db_table = 'MEMBER_INFO_TABLE'


class ActivityPeriod(models.Model):

    """Model- ActivityPeriod"""

    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='activity_periods')

    class Meta:
        db_table = 'ACTIVITY_PERIOD_INFO_TABLE'




