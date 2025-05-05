from django.db import models
from django.core.validators import MinValueValidator

class Game(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    designer = models.CharField(max_length=200)
    year = models.IntegerField(validators=[MinValueValidator(1900)])
    players = models.IntegerField(validators=[MinValueValidator(1)])
    play_time = models.IntegerField(validators=[MinValueValidator(1)])
    age = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.title}"