from rest_framework import generics, viewsets, status, views
from rest_framework.permissions import IsAuthenticated
from .models import Tournament, Ranking
from .serializers import TournamentSerializer, RankingSerializer, Match, MatchSerializer
from .permissions import IsAdminUser
from rest_framework.response import Response


class FilteredRankingView(views.APIView):
    "Statistics of Players"
    permission_classes = [IsAuthenticated]
    def get(self, request):
        tournament_id = request.query_params.get('tournament_id', None)
        participant_id = request.query_params.get('participant_id', None)
        rankings = Ranking.objects.all()
        if tournament_id:
            rankings = rankings.filter(tournament_id=tournament_id)
        
        if participant_id:
            rankings = rankings.filter(participant_id=participant_id)

        serializer = RankingSerializer(rankings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser] 

class RankingViewSet(viewsets.ModelViewSet):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
    permission_classes = [IsAuthenticated, IsAdminUser] 

class GeneratePairingsView(views.APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, tournament_id):
        try:
            tournament = Tournament.objects.get(id=tournament_id)
        except Tournament.DoesNotExist:
            return Response({"error": "Tournament not found"}, status=status.HTTP_404_NOT_FOUND)
        
        participants = list(tournament.participiants.all())
        
        # Pairings logic for Swiss-system tournament
        matches = []
        while len(participants) >= 2:
            white = participants.pop()
            black = participants.pop()
            match = Match.objects.create(tournament=tournament, black=black, white=white)
            matches.append(match)
        
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)