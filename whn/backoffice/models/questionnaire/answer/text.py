from django.db import models
from .answer import Answer


class Text(Answer):
    body = models.TextField()
    