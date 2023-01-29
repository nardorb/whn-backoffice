from django.db import models

from patient_record import PatientRecord


class HouseholdInfo(models.Model):
    control_num = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    marital_status = None
    number_of_children = None
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
