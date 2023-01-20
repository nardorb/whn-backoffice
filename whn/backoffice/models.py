from django.db import models


class PatientRec(models.Model):
    """Maintains patient record information and identifiers"""
    control_num = models.UUIDField()
    status = models.CharField()
    notes = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class PatientBio(models.Model):
    """Maintains patient biographical information"""
    control_num = models.ForeignKey('PatientRec', on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    dob = models.DateField()
    sex = models.CharField(max_length=1)
    nationality = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    # ToDo: Implement to string for full name.
    # ToDo: Implement class method to returnn current age.


class Dependent(models.Model):
    """Maintains patient dependent information"""
    control_num = models.ForeignKey('PatientRec', on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    dob = models.DateField()
    sex = models.CharField(max_length=1)

    # ToDo: Implement to string for full name.
    # ToDo: Implement class method to returnn current age.


class NOK(models.Model):
    """Maintains patient next-of-kin"""
    None


class Contact(models.Model):
    """Maintains patient contact information. Record either holds a phone number or an email address"""
    control_num = models.ForeignKey('PatientRec', on_delete=models.CASCADE)
    type = models.CharField()  # Contact type eg: work, cell, home.
    number = models.CharField()  # Fully formatted number
    email = models.EmailField()  # Email address

    # ToDo: Implement save function override to auto format number or reject save on failure.
    # ToDo: Implement function to enforce that only one contact type exists in each instance.


class Address(models.Model):
    control_num = models.ForeignKey('PatientRec', on_delete=models.CASCADE)
    type = models.CharField()  # Address type
    line1 = models.CharField()
    line2 = models.CharField()
    city = models.CharField()
    state = models.CharField()
    postal_code = models.CharField()
    country = models.CharField()


class Employment(models.Model):
    control_num = models.ForeignKey('PatientRec', on_delete=models.CASCADE)
    type = models.CharField()  # Employment type
    employer = models.CharField()
    position = models.CharField()


class HealthSeekingInfo(models.Model):
    control_num = models.ForeignKey('PatientRec', on_delete=models.CASCADE)


class SocialInclusion(models.Model):
    control_num = models.ForeignKey('PatientRec', on_delete=models.CASCADE)


class CommunityInclusionInfo(models.Model):
    control_num = models.ForeignKey('PatientRec', on_delete=models.CASCADE)


class HouseholdInfo(models.Model):
    control_num = models.ForeignKey('PatientRec', on_delete=models.CASCADE)


class MedicalHistory(models.Model):
    control_num = models.ForeignKey('PatientRec', on_delete=models.CASCADE)
