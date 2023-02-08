from django.db import models

from .patient_record import PatientRecord


class Address(models.Model):
    """Maintains patient address information."""
    HOME = 'HM'
    MAILING = 'ML'
    TEMPORARY = 'TM'
    WORK = 'WK'

    ADDRESS_TYPE_CHOICES = [
        (HOME, 'Home Address'),
        (MAILING, 'Mailing Address'),
        (TEMPORARY, 'Temporary Address'),
        (WORK, 'Work Address'),
    ]

    id = models.UUIDField(primary_key=True)
    control_num = models.ForeignKey(
        PatientRecord,
        on_delete=models.CASCADE
    )
    type = models.CharField(
        max_length=2,
        choices=ADDRESS_TYPE_CHOICES,
        default=HOME,
    )
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=15)
    country = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
