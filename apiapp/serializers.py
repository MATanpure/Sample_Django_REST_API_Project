from rest_framework.serializers import ModelSerializer
from .models import Member, ActivityPeriod


class ActivityPeriodSerializer(ModelSerializer):
    """serializer class for Activity Periods"""

    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class MemberSerializer(ModelSerializer):
    """serializer class for Members"""

    class Meta:
        model = Member
        fields = ['id', 'real_name', 'tz', 'activity_periods']

    activity_periods = ActivityPeriodSerializer(read_only=True, many=True)

