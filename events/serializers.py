from rest_framework import serializers
from django.shortcuts import get_object_or_404
from caregivers.models import CareGiver
from .models import EventType
from .models import Event


class EventSerializer(serializers.Serializer):
    care_giver_name = serializers.StringRelatedField(source='care_giver.name')
    event_type_name = serializers.StringRelatedField(source='event_type.name')
    time_stamp = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Event

    def create(self, validated_data):
        """
        Create and return a new `Event` instance, given the validated data.
        """
        care_giver = get_object_or_404(CareGiver, name=validated_data['care_giver_name'])
        event_type = get_object_or_404(EventType, name=validated_data['event_type_name'])
        return Event.objects.create(care_giver=care_giver, event_type=event_type)
