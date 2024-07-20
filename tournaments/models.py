from django.db import models
import uuid
from users.models import CustomUser

class Tournament(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participiants = models.ManyToManyField(
        CustomUser,
        verbose_name="User",
        related_name="tournaments",
        blank=True,
    )
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.id

class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="matches")
    black = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="matches_as_black")
    white = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="matches_as_white")
    is_black_won = models.BooleanField(default=False)
    is_white_won = models.BooleanField(default=False)
    is_draw = models.BooleanField(default=False)

    def __str__(self):
        return f"Match {self.id} in Tournament {self.tournament.id}"

class Ranking(models.Model):
    participiant = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="ranks")
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="ranks")
    plays = models.IntegerField()
    rank = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    loses = models.IntegerField()


