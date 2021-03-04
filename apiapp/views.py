from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MemberSerializer, ActivityPeriodSerializer
from .models import Member, ActivityPeriod


class MemberCRUDViewSet(ModelViewSet):
    """Class based view for member CRUD operations"""

    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class ActivityPeriodCRUDViewSet(ModelViewSet):
    """Class based view for activity periods CRUD operations"""

    serializer_class = ActivityPeriodSerializer
    queryset = ActivityPeriod.objects.all()




