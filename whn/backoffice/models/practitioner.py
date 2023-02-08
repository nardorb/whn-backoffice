from django.db import models


class Practitioner(models.Model):
    """Maintains practitioner information and status"""
    ACTIVE = 'A'
    INACTIVE = 'I'
    UNDER_REVIEW = 'R'
    DELETED = 'D'

    ADMIN = 'A'
    CLERK = 'C'
    DOCTOR = 'D'
    NURSE = 'N'
    VOLUNTEER = 'V'

    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (UNDER_REVIEW, 'Under Review'),
        (DELETED, 'Deleted')
    ]

    ROLE_CHOICES = [
        (ADMIN, 'Administrator'),
        (CLERK, 'Office Clerk'),
        (DOCTOR, 'Doctor'),
        (NURSE, 'Nurse'),
        (VOLUNTEER, 'Volunteer')
    ]

    id = models.UUIDField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=255,
        unique=True,
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=ACTIVE
    )
    role = models.CharField(
        max_length=1,
        choices=ROLE_CHOICES
    )
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
