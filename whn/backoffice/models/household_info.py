from django.db import models

from .patient_record import PatientRecord


class HouseholdInfo(models.Model):
    """Maintains patient household information."""
    SINGLE = 'SI'
    MARRIED = 'MR'
    DIVORCED = 'DI'
    WIDOWED = 'WI'
    COMMON_LAW = 'CL'

    MARITAL_STATUS_CHOICES = [
        (SINGLE, 'Single'),
        (MARRIED, 'Married'),
        (DIVORCED, 'Divorced'),
        (WIDOWED, 'Widowed'),
        (COMMON_LAW, 'Common-Law')
    ]

    id = models.UUIDField(primary_key=True)
    control_num = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    marital_status = models.CharField(
        max_length=2,
        choices=MARITAL_STATUS_CHOICES,
        default=SINGLE
    )
    number_of_children = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
