from django.db import models

from .practitioner import Practitioner


class PatientRecord(models.Model):
    """Maintains patient record information and identifiers"""
    ACTIVE = 'A'
    INACTIVE = 'I'
    UNDER_REVIEW = 'R'
    DELETED = 'D'

    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (UNDER_REVIEW, 'Under Review'),
        (DELETED, 'Deleted')
    ]

    control_num = models.UUIDField(primary_key=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=ACTIVE
    )
    notes = models.TextField()
    registered_by = models.ForeignKey(
        Practitioner,
        on_delete=models.SET_NULL,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
