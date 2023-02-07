from django.db import models

from .patient_record import PatientRecord


class NextOfKin(models.Model):
    """Maintains patient next-of-kin"""
    id = models.UUIDField(primary_key=True)
    control_num = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
