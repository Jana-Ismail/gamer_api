from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=255)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = ("game", "user")
        verbose_name = "Game Review"
        verbose_name_plural = "Game Reviews"
        ordering = ['-created']
    
    def __str__(self):
        return f"Review by {self.user.username} of {self.game.title} on {self.created}"