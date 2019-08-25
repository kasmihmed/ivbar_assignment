from collections import defaultdict
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from caregivers.models import CareGiver
from events.serializers import EventSerializer
from .models import Event
from django.shortcuts import get_object_or_404


class EventView(viewsets.ViewSet):

    def list(self, request):
        events = Event.objects.filter(self._filter_q(request))\
            .select_related('event_type', 'care_giver')
        sums_by_month_caregiver = defaultdict(lambda: defaultdict(int))
        for event in events:
            month = event.time_stamp.month
            caregiver_name = event.care_giver.name
            sums_by_month_caregiver[month][caregiver_name] += \
                event.event_type.reimbursement_amount
        return Response(sums_by_month_caregiver)

    def _filter_q(self, request):
        caregiver_names = request.query_params.get('caregivers', None)
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        filter_q = Q()
        if caregiver_names is not None:
            caregiver_names = caregiver_names.split(',')
            filter_q &= Q(care_giver__name__in=caregiver_names)
        if start_date is not None:
            filter_q &= Q(time_stamp__gte=start_date)
        if end_date is not None:
            filter_q &= Q(time_stamp__lte=end_date)
        return filter_q

    def create(self, request, caregiver_id):
        data = JSONParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            data['care_giver'] = get_object_or_404(CareGiver, pk=caregiver_id)
            serializer.save(**data)
            return Response(status=201)
        return Response(serializer.errors, status=400)
