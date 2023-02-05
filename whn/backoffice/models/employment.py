from django.db import models

from patient_record import PatientRecord


class Employment(models.Model):
    id = models.UUIDField()
    control_num = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    type = models.CharField()  # Employment type
    employer = models.CharField()
    position = models.CharField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
