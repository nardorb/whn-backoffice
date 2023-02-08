from django.db import models

from .patient_record import PatientRecord


class Email(models.Model):
    """Maintains patient email address."""
    PERSONAL = 'PE'
    BUSINESS = 'BE'
    WORK = 'WK'

    EMAIL_TYPE_CHOICES = [
        (PERSONAL, 'Personal Email'),
        (BUSINESS, 'Business Email'),
        (WORK, 'Work Email'),
    ]

    id = models.UUIDField(primary_key=True)
    type = models.CharField(
        max_length=2,
        choices=EMAIL_TYPE_CHOICES,
        default=PERSONAL,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    control_num = models.ForeignKey(
        PatientRecord,
        on_delete=models.CASCADE
    )
