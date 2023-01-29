from django.db import models

from patient_record import PatientRecord


class Address(models.Model):
    id = models.UUIDField()
    control_num = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    type = models.CharField()  # Address type
    line1 = models.CharField()
    line2 = models.CharField()
    city = models.CharField()
    state = models.CharField()
    postal_code = models.CharField()
    country = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
