from django.core.validators import MinValueValidator
from django.db import models
from caregivers.models import CareGiver


class EventType(models.Model):
    # currency is assumed to be fixed to SEK for now
    name = models.CharField(max_length=100)
    reimbursement_amount = models.FloatField(blank=False, null=False, validators=[MinValueValidator(0)])


class Event(models.Model):
    care_giver = models.ForeignKey(CareGiver) # TODO: check delete strategy
    event_type = models.ForeignKey(EventType) # TODO: check delete strategy
    time_stamp = models.DateTimeField(auto_now_add=True)

