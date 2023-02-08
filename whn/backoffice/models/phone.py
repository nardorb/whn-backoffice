from django.db import models

from .patient_record import PatientRecord


class Phone(models.Model):
    """Maintains patient contact information."""
    HOME = 'HP'
    CELL = 'CP'
    WORK = 'WK'

    PHONE_TYPE_CHOICES = [
        (HOME, 'Home Phone'),
        (CELL, 'Cell Phone'),
        (WORK, 'Work Phone'),
    ]

    id = models.UUIDField(primary_key=True)
    type = models.CharField(
        max_length=2,
        choices=PHONE_TYPE_CHOICES,
        default=CELL,
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    control_num = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
