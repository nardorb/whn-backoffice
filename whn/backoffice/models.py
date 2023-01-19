from django.db import models


class PatientRec(models.Model):
    """Maintains patient record information and identifiers"""
    control_num = models.UUIDField()
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    dob = models.DateField()
    sex = models.CharField(max_length=1)
    nationality = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class PatientBio(models.Model):
    None


class Dependent(models.Model):
    None


class Contact(models.Model):
    None


class Address(models.Model):
    None


class Employment(models.Model):
    None


class HealthSeekingInfo(models.Model):
    None


class SocialInclusion(models.Model):
    None


class CommunityInclusionInfo(models.Model):
    None


class HouseholdInfo(models.Model):
    None


class MedicalHistory(models.Model):
    None