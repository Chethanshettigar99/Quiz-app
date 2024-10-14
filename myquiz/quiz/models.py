from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    QUESTION_TYPES = [
        ('MCQ', 'Multiple Choice'),
        ('DESC', 'Descriptive')
    ]

    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=20, blank=True, null=True)
    option2 = models.CharField(max_length=20, blank=True, null=True)
    option3 = models.CharField(max_length=20, blank=True, null=True)
    option4 = models.CharField(max_length=20, blank=True, null=True)
    answer = models.CharField(max_length=20)
    type = models.CharField(max_length=4, choices=QUESTION_TYPES, default='MCQ')

    def __str__(self):
        return self.question
