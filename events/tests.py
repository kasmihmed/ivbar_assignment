from rest_framework.test import APIClient
from django.test import TestCase
from caregivers.models import CareGiver
from events.models import EventType, Event

class TestEvents(TestCase):

    def setUp(self):
        EventType.objects.create(name='event_type', reimbursement_amount=500)
        return CareGiver.objects.create(name='caregiver_name', location='caregiver_location')

    def test_create_events(self):
        client = APIClient()
        assert Event.objects.count() == 0
        response = client.post('/caregivers/1/events/', {'event_type': 'event_type'}, format='json')
        assert response.status_code == 201
        assert Event.objects.count() == 1
        event = Event.objects.first()
        assert event.event_type.name == "event_type"
        assert event.care_giver_id == 1

    def test_get_available_events(self):
        client = APIClient()
        assert Event.objects.count() == 0
        response = client.get('/events/')
        assert response.status_code == 200
        # The report should be empty in the begining
        assert response.json() == {}
        response = client.post('/caregivers/1/events/', {'event_type': 'event_type'}, format='json')
        assert response.status_code == 201
        assert Event.objects.count() == 1
        response = client.get('/events/')
        events_by_month_caregiver = response.json()
        assert len(events_by_month_caregiver.keys()) == 1
        assert len(events_by_month_caregiver['8'].keys()) == 1
        assert events_by_month_caregiver['8']['caregiver_name'] == 500


