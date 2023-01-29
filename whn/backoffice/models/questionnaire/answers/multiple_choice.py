from django.db import models
from whn.backoffice.models.questionnaire.answers.answer import Answer


class MultipleChoice(Answer):
    body = models.MultipleChoiceField()
