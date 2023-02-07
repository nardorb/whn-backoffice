from django.contrib import admin

from .models.address import Address
from .models.dependent import Dependent
from .models.email import Email
from .models.employment import Employment
from .models.household_info import HouseholdInfo
from .models.next_of_kin import NextOfKin
from .models.patient_bio import PatientBio
from .models.patient_record import PatientRecord
from .models.questionnaire.question import Question
from .models.questionnaire.answer.float import Float
from .models.questionnaire.answer.number import Number
from .models.questionnaire.answer.short_text import ShortText
from .models.questionnaire.answer.text import Text

# Patient Record
admin.site.register(Address)
admin.site.register(Dependent)
admin.site.register(Email)
admin.site.register(Employment)
admin.site.register(HouseholdInfo)
admin.site.register(NextOfKin)
admin.site.register(PatientBio)
admin.site.register(PatientRecord)

# Questionnaire
admin.site.register(Question)
admin.site.register(Float)
admin.site.register(Number)
admin.site.register(ShortText)
admin.site.register(Text)
