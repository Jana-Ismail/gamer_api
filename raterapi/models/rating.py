from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Rating(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ratings")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="ratings")

    class Meta:
        # Prevent users from rating the same game multiple times
        unique_together = ("user", "game")
        verbose_name = "Game Rating"
        verbose_name_plural = "Game Ratings"
    
    def __str__(self):
        return f"{self.user.username}'s rating for {self.game.title}: {self.rating}"