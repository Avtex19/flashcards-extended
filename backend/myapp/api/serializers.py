from rest_framework import serializers

from ..models import Flashcard, Category, Deck, CustomUser, Hint


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DeckSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Deck
        fields = '__all__'


class FlashcardSerializer(serializers.ModelSerializer):
    deck = serializers.PrimaryKeyRelatedField(queryset=Deck.objects.all())

    class Meta:
        model = Flashcard
        fields = '__all__'


class HintSerializer(serializers.ModelSerializer):
    flashcard = serializers.PrimaryKeyRelatedField(queryset=Flashcard.objects.all())

    class Meta:
        model = Hint
        fields = '__all__'
