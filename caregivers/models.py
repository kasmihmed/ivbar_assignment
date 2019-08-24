from django.db import models


class CareGiver(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField(max_length=500)

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name
