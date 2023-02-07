from django.db import models
from .answer import Answer


class ShortText(Answer):
    body = models.CharField(max_length=255)
