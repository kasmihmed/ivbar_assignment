from collections import defaultdict
from itertools import groupby
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from caregivers.models import CareGiver
from events.serializers import EventSerializer
from .models import Event
from django.shortcuts import get_object_or_404


class EventView(viewsets.ViewSet):

    def list(self, request):
        events = Event.objects.all().select_related('event_type')
        sums_by_month_caregiver = defaultdict(lambda: defaultdict(int))
        for event in events:
            sums_by_month_caregiver[event.time_stamp.month][event.care_giver.name] += event.event_type.reimbursement_amount
        return Response(sums_by_month_caregiver)

    def create(self, request, caregiver_id):
        data = JSONParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            data['care_giver_name'] = get_object_or_404(CareGiver, pk=caregiver_id).name
            data['event_type_name'] = data.pop('event_type')
            serializer.save(**data)
            return Response(status=201)
        return Response(serializer.errors, status=400)