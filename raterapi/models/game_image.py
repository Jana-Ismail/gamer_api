# from django.db import models
# from django.contrib.auth.models import User

# class GameImage(models.model):
#     game = models.ForeignKey("Game", on_delete=models.DO_NOTHING, related_name="images")
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#     url = models.URLField()

#     class Meta:
#         verbose_name = "Game Image"
#         verbose_name_plural = "Game Images"