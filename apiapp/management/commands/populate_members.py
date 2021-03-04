from apiapp.models import Member
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from random import choice
from faker import Faker


faker = Faker()
tzs = ["Africa/Addis_Ababa", "America/Aruba", "America/Los_Angeles", "Asia/Calcutta", "Canada/Yukon"]
ids = ["W012A3CDE", "W07QCRPA4", "W03ABMCE5", "W05QCRPV9", "W08QCRP6K",
       "W035A3CFB", "W09QCRPB8", "W06ABMCZ9", "W04QCRPM5", "W2MQCRPL9",]


class Command(BaseCommand):

    """Custom management command for populating members."""

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of members to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            fid = choice(ids)
            fname = faker.name()
            ftz = choice(tzs)
            member_record = Member(id=fid, real_name=fname, tz=ftz)
            member_record.save()
