from django.db import models
from whn.backoffice.models.questionnaire.answers.answer import Answer


class Number(Answer):
    body = models.IntegerField()
