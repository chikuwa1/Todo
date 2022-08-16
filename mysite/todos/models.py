from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

PRIOLITY_COICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class Todo(models.Model):
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=200)
    deadline = models.DateTimeField('締め切り')
    priolity = models.IntegerField(choices = PRIOLITY_COICES, default = 3)
    
    def __str__(self):
        return self.name
    
    # @property
    # def is_past_deadline(self):
    #     return datetime.datetime.now() > self.deadline
