from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ..api.views import FlashcardViewSet, DeckViewSet, CategoryViewSet, HintViewSet

router = DefaultRouter()
router.register('flashcards', FlashcardViewSet, 'flashcard')
router.register('decks', DeckViewSet)
router.register('categories', CategoryViewSet)
router.register('hints', HintViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
