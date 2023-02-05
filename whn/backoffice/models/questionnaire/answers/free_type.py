from django.db import models
from whn.backoffice.models.questionnaire.answers.answer import Answer


class FreeType(Answer):
    body = models.TextField(max_length=255)
