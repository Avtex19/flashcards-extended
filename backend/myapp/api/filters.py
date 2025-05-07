import django_filters
from ..models import Flashcard, Deck


class DeckFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(field_name='category')

    class Meta:
        model = Deck
        fields = ['category']


class FlashcardFilter(django_filters.FilterSet):
    deck = django_filters.NumberFilter(field_name='deck')
    category = django_filters.NumberFilter(
        field_name='deck__category') # 'deck__category' means: filter flashcards by their deck's category
    # (Flashcard  → Deck → Category)


    class Meta:
        model = Flashcard
        fields = ['deck', 'category']
