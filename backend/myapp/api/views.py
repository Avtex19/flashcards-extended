from rest_framework import viewsets

from .serializers import FlashcardSerializer, CategorySerializer, DeckSerializer, HintSerializer
from ..models import Flashcard, Category, Deck, Hint


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeckViewSet(viewsets.ModelViewSet):
    serializer_class = DeckSerializer
    queryset = Deck.objects.all()

    def get_queryset(self):
        category_id = self.request.query_params.get('category')
        if category_id:
            return Deck.objects.filter(category_id=category_id)
        return Deck.objects.all()


class FlashCardViewSet(viewsets.ModelViewSet):
    serializer_class = FlashcardSerializer

    def get_queryset(self):
        deck_id = self.request.query_params.get('deck')
        category_id = self.request.query_params.get('category')
        if deck_id:
            queryset = Flashcard.objects.filter(deck_id=deck_id)
        if category_id:
            queryset = Flashcard.objects.filter(deck__category_id=category_id)
        return queryset


class HintViewSet(viewsets.ModelViewSet):
    queryset = Hint.objects.all()
    serializer_class = HintSerializer
