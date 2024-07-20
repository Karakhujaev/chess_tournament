from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import CustomUser
from tournaments.models import Tournament, Match, Ranking

class TournamentTests(APITestCase):
    def setUp(self):
        self.admin_user = CustomUser.objects.create_user(username='admin', password='adminpass', is_admin=True)
        self.regular_user = CustomUser.objects.create_user(username='user', password='userpass')
        self.client = APIClient()
    
    def test_create_tournament(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('tournament-list-create')
        data = {'is_active': True}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_tournaments(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('tournament-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class MatchTests(APITestCase):
    def setUp(self):
        self.admin_user = CustomUser.objects.create_user(username='admin', password='adminpass', is_admin=True)
        self.client = APIClient()
        self.tournament = Tournament.objects.create(is_active=True)

    def test_create_match(self):
        self.client.force_authenticate(user=self.admin_user)
        white = CustomUser.objects.create_user(username='white', password='whitepass')
        black = CustomUser.objects.create_user(username='black', password='blackpass')
        url = reverse('match-list-create')
        data = {'tournament': self.tournament.id, 'white': white.id, 'black': black.id, 'is_white_won': False, 'is_black_won': False, 'is_draw': False}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_matches(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('match-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_match_result(self):
        self.client.force_authenticate(user=self.admin_user)
        white = CustomUser.objects.create_user(username='white', password='whitepass')
        black = CustomUser.objects.create_user(username='black', password='blackpass')
        match = Match.objects.create(tournament=self.tournament, white=white, black=black)
        url = reverse('match-detail', args=[match.id])
        data = {'tournament': self.tournament.id, 'white': white.id, 'black': black.id, 'is_white_won': True, 'is_black_won': False, 'is_draw': False}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PairingTests(APITestCase):
    def setUp(self):
        self.admin_user = CustomUser.objects.create_user(username='admin', password='adminpass', is_admin=True)
        self.client = APIClient()
        self.tournament = Tournament.objects.create(is_active=True)
        self.participant1 = CustomUser.objects.create_user(username='participant1', password='participant1pass')
        self.participant2 = CustomUser.objects.create_user(username='participant2', password='participant2pass')
        self.participant3 = CustomUser.objects.create_user(username='participant3', password='participant3pass')
        self.participant4 = CustomUser.objects.create_user(username='participant4', password='participant4pass')
        self.tournament.participiants.add(self.participant1, self.participant2, self.participant3, self.participant4)

    def test_generate_pairings(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('generate-pairings', args=[self.tournament.id])
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Match.objects.filter(tournament=self.tournament).count(), 2)

class RankingTests(APITestCase):
    def setUp(self):
        self.admin_user = CustomUser.objects.create_user(username='admin', password='adminpass', is_admin=True)
        self.client = APIClient()
        self.tournament = Tournament.objects.create(is_active=True)
        self.participant = CustomUser.objects.create_user(username='participant', password='participantpass')
        self.ranking = Ranking.objects.create(participant=self.participant, tournament=self.tournament, plays=0, rank=1, wins=0, draws=0, loses=0)

    def test_get_filtered_rankings_by_tournament_id(self):
        self.client.force_authenticate(user=self.admin_user)
        url = f'/api/filtered-rankings/?tournament_id={self.tournament.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_filtered_rankings_by_participant_id(self):
        self.client.force_authenticate(user=self.admin_user)
        url = f'/api/filtered-rankings/?participant_id={self.participant.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
