from django.db import models

from .patient_record import PatientRecord


class Dependent(models.Model):
    """Maintains patient dependent information"""
    id = models.UUIDField(primary_key=True)
    control_num = models.ForeignKey(
        PatientRecord,
        on_delete=models.CASCADE
    )
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    dob = models.DateField()
    sex = models.CharField(max_length=1)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # ToDo: Implement to string for full name.
    # ToDo: Implement class method to returnn current age.
