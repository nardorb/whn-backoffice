import pycountry

from django.db import models

from .patient_record import PatientRecord


class PatientBio(models.Model):
    """Maintains patient biographical information"""
    MALE = 'M'
    FEMALE = 'F'

    SEX_CHOICES = [
        (FEMALE, 'Female'),
        (MALE, 'Male')
    ]

    id = models.UUIDField(primary_key=True)
    control_num = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    dob = models.DateField()
    sex = models.CharField(
        max_length=2,
        choices=SEX_CHOICES
    )
    nationality = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # ToDo: Implement to string for full name.
    # ToDo: Implement class method to returnn current age.
