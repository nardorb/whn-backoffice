from django.db import models


class Question(models.Model):
    COMMUNITY_ENVIRONMENT = 'CE'
    HEALTH_SEEKING_BEHAVIOUR = 'HE'
    HOUSEHOLD = 'HH'
    SOCIAL_INCLUSION = 'SI'
    QUESTION_TYPE_CHOICES = [
        (COMMUNITY_ENVIRONMENT, 'Community Environment'),
        (HEALTH_SEEKING_BEHAVIOUR, 'Health Seeking Behaviour'),
        (HOUSEHOLD, 'Household Data'),
        (SOCIAL_INCLUSION, 'Social Inclusion'),
    ]
    category = models.CharField(
        max_length=2,
        choices=QUESTION_TYPE_CHOICES,
    )
    id = models.UUIDField()
    question_body = models.CharField(max_length=255)
    choices = models.Many
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
