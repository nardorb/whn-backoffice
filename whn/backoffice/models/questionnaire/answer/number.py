from django.db import models
from .answer import Answer


class Number(Answer):
    body = models.IntegerField()
