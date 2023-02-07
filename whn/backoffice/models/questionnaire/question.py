from django.db import models


class Question(models.Model):
    """Represents a question in a questionnaire. The answer of which will form a part
    of the patient record and instruct practitioners on diagnosis and treatment options
    which will form a part of """
    # List of question types
    COMMUNITY_ENVIRONMENT = 'CE'
    HEALTH_SEEKING_BEHAVIOUR = 'HE'
    HOUSEHOLD = 'HH'
    SOCIAL_INCLUSION = 'SI'

    # List of answer types
    CHOICE = 'CH'
    FLOAT = 'FL'
    FREE_TYPE = 'FT'
    MULTI_CHOICE = 'MC'
    MULTIPLE_CHOICE_TEXT = 'MT'
    NUMBER = 'NB'
    TEXT = 'TX'

    QUESTION_TYPE_CHOICES = [
        (COMMUNITY_ENVIRONMENT, 'Community Environment'),
        (HEALTH_SEEKING_BEHAVIOUR, 'Health Seeking Behaviour'),
        (HOUSEHOLD, 'Household Data'),
        (SOCIAL_INCLUSION, 'Social Inclusion'),
    ]

    ANSWER_TYPE_CHOICES = [
        (CHOICE, 'Choice Field'),
        (FLOAT, 'Floating Point Number Field'),
        (FREE_TYPE, 'Free Type Text Field'),
        (MULTI_CHOICE, 'Multiple Choice Field'),
        (MULTIPLE_CHOICE_TEXT, 'Multiple Choice Text Field'),
        (NUMBER, 'Number Field'),
        (TEXT, 'Text Field'),
    ]

    id = models.UUIDField(primary_key=True)
    category = models.CharField(
        max_length=2,
        choices=QUESTION_TYPE_CHOICES,
    )
    answer_type = models.CharField(
        max_length=2,
        choices=ANSWER_TYPE_CHOICES,
    )
    question_body = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

# ToDo: Add Method to retrieve answer object based on choice.
