from django.db import models
from whn.backoffice.models.questionnaire.answers.answer import Answer


class Text(Answer):
    body = models.CharField(max_length=255)
    