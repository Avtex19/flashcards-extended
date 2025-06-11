from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filters import FlashcardFilter, DeckFilter
from .serializers import FlashcardSerializer, CategorySerializer, DeckSerializer, HintSerializer
from ..models import Flashcard, Category, Deck, Hint


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DeckFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FlashcardViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Flashcard.objects.all()
    serializer_class = FlashcardSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FlashcardFilter


class HintViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Hint.objects.all()
    serializer_class = HintSerializer
