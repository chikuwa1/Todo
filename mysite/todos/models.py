from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Todo(models.Model):
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=200)
    deadline = models.DateTimeField('締め切り')
    #priolity = models.IntegerField(default=1,validators=[MinValueValidator(1), MaxValueValidator(5)])
    
    def __str__(self):
        return self.name
