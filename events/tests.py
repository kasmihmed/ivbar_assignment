from rest_framework.test import APIClient
from django.test import TestCase
from caregivers.models import CareGiver
from events.models import EventType, Event
from dateutil.relativedelta import relativedelta


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
        month = list(events_by_month_caregiver.keys())[0]
        assert len(events_by_month_caregiver[month].keys()) == 1
        assert events_by_month_caregiver[month]['caregiver_name'] == 500

    def test_filtering_by_month(self):
        client = APIClient()
        response = client.post('/caregivers/1/events/', {'event_type': 'event_type'}, format='json')
        assert response.status_code == 201
        response = client.post('/caregivers/1/events/', {'event_type': 'event_type'}, format='json')
        assert response.status_code == 201
        assert Event.objects.count() == 2
        # change the date of the first event to 1 month earlier
        first_event = Event.objects.first()
        first_event.time_stamp = first_event.time_stamp + relativedelta(months=1)
        first_event.save()
        response = client.get('/events/')
        events_by_month_caregiver = response.json()
        assert len(events_by_month_caregiver.keys()) == 2
        first_month = list(events_by_month_caregiver.keys())[0]
        second_month = list(events_by_month_caregiver.keys())[1]
        assert len(events_by_month_caregiver[first_month].keys()) == 1
        assert int(first_month) - int(second_month) == -1 or int(first_month) - int(second_month) == 1
        assert events_by_month_caregiver[first_month]['caregiver_name'] == 500
        assert len(events_by_month_caregiver[second_month].keys()) == 1
        assert events_by_month_caregiver[second_month]['caregiver_name'] == 500



    def test_filtering_by_caregiver(self):
        client = APIClient()
        CareGiver.objects.create(name='caregiver_name 2', location='caregiver_location 2')
        response = client.post('/caregivers/1/events/', {'event_type': 'event_type'}, format='json')
        assert response.status_code == 201
        response = client.post('/caregivers/2/events/', {'event_type': 'event_type'}, format='json')
        assert response.status_code == 201
        assert Event.objects.count() == 2
        # change the date of the first event to 1 month earlier
        first_event = Event.objects.first()
        response = client.get('/events/')
        events_by_month_caregiver = response.json()
        assert len(events_by_month_caregiver.keys()) == 1
        month = list(events_by_month_caregiver.keys())[0]
        assert len(events_by_month_caregiver[month].keys()) == 2
        assert events_by_month_caregiver[month]['caregiver_name'] == 500
        assert events_by_month_caregiver[month]['caregiver_name 2'] == 500



