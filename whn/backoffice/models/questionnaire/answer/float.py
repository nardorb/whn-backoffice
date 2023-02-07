from django.db import models

from .answer import Answer


class Float(Answer):
    body = models.FloatField()
