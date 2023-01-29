from django.db import models
from whn.backoffice.models.questionnaire.answers.answer import Answer


class MultipleChoiceText(Answer):
    body = models.TypedMultipleChoiceField()
