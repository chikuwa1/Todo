from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

PRIOLITY_COICES = (
    (1, '１(低い)'),
    (2, '２(少し低い)'),
    (3, '３(普通)'),
    (4, '４(少し高い)'),
    (5, '５(高い)'),
)

class Todo(models.Model):
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=200)
    deadline = models.DateTimeField('締め切り')
    priolity = models.IntegerField(choices = PRIOLITY_COICES, default = 3)
    
    def __str__(self):
        return self.name
