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
    name = models.CharField(max_length=50) #やるべきこと
    detail = models.CharField(max_length=200) #内容・詳細
    deadline = models.DateTimeField('締め切り') #締め切り
    priolity = models.IntegerField(choices = PRIOLITY_COICES, default = 3) #優先順位
    
    def __str__(self):
        return self.name
    
