from apiapp.models import Member, ActivityPeriod
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from random import choice
from faker import Faker

start_times = ["Feb 1 2020 1:33PM", "Feb 2 2020 2:35PM", "Feb 3 2020 3:43PM", "Feb 10 2020 5:50PM"]
end_times = ["Mar 1 2020 1:33PM", "Mar 2 2020 2:35PM", "Mar 3 2020 3:43PM", "Mar 10 2020 5:50PM"]
ids = ["W012A3CDE", "W07QCRPA4", "W03ABMCE5", "W05QCRPV9", "W08QCRP6K",
       "W035A3CFB", "W09QCRPB8", "W06ABMCZ9", "W04QCRPM5", "W2MQCRPL9"]


class Command(BaseCommand):

    """Custom management command for populating activity periods."""

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of activity periods to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            fstart_time = choice(start_times)
            fend_time = choice(end_times)
            member = Member.objects.get(id=choice(ids))
            activity_period_record = ActivityPeriod(start_time=fstart_time, end_time=fend_time, member=member)
            activity_period_record.save()