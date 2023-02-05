from django.db import models
from ..question import Question
from whn.backoffice.models.patient_record import PatientRecord


class Answer(models.Model):
    id = models.UUIDField()
    patient_id = models.ForeignKey(PatientRecord, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
