from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TournamentViewSet, RankingViewSet, FilteredRankingView

router = DefaultRouter()
router.register(r'tournaments', TournamentViewSet)
router.register(r'rankings', RankingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('filtered-rankings/', FilteredRankingView.as_view(), name='filtered-ranking'),
]