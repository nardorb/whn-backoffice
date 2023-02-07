from django.db import models

from .patient_record import PatientRecord


class Employment(models.Model):
    """Maintains patient current employment information."""
    PERMANENT = 'PR'
    TEMPORARY = 'TM'
    CONTRACT = 'CT'
    UNEMPLOYED = 'UE'

    EMPLOYMENT_TYPE_CHOICES = [
        (PERMANENT, 'Permanent'),
        (TEMPORARY, 'Temporary'),
        (CONTRACT, 'Contract'),
        (UNEMPLOYED, 'Unemployed')
    ]

    id = models.UUIDField(primary_key=True)
    control_num = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=2,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default=PERMANENT
    )
    employer = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
