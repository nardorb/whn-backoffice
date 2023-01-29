from django.db import models


class PatientRecord(models.Model):
    """Maintains patient record information and identifiers"""
    control_num = models.UUIDField()
    status = models.CharField()
    notes = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
