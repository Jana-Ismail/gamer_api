from django.db import models

class GameCategory(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="categories")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="games")

    class Meta:
        unique_together = ("game", "category")
        verbose_name_plural = "Game Cateogories"
    
    def __str__(self):
        return f"{self.game.title} - "