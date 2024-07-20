from rest_framework import serializers
from .models import Tournament, CustomUser, Ranking, Match

class TournamentSerializer(serializers.ModelSerializer):
    participiants = serializers.PrimaryKeyRelatedField(
        many=True, queryset=CustomUser.objects.all()
    )
    class Meta:
        model = Tournament
        fields = ["id", "participiants", "start", "end"]

class RankingSerializer(serializers.ModelSerializer):
    tournament = serializers.PrimaryKeyRelatedField(queryset=Tournament.objects.all())
    participiant = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    class Meta:
        model = Tournament
        fields = ["id", "participiant", "tournament", "wins", "draws", "loses", "plays"]


class MatchSerializer(serializers.ModelSerializer):
    tournament = serializers.PrimaryKeyRelatedField(queryset=Tournament.objects.all())
    black = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    white = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    class Meta:
        model = Tournament
        fields = ["id", "tournament", "black", "white", "is_black_won", "is_white_won"]