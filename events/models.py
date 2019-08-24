from django.core.validators import MinValueValidator
from django.db import models
from caregivers.models import CareGiver


class EventType(models.Model):
    # currency is assumed to be fixed to SEK for now
    name = models.CharField(max_length=100)
    reimbursement_amount = models.FloatField(blank=False, null=False, validators=[MinValueValidator(0)])

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name


class Event(models.Model):
    care_giver = models.ForeignKey(CareGiver, on_delete=models.PROTECT)
    event_type = models.ForeignKey(EventType, on_delete=models.PROTECT)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} from {self.care_giver} ({self.time_stamp})"

