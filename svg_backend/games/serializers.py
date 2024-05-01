from rest_framework import serializers
from .models import Game
from rest_framework.response import Response


class GameSerializer(serializers.ModelSerializer):
    """Serializer for the Game model."""
    class Meta:
        model = Game
        fields = '__all__'
        extra_kwargs = {
            'name': {'error_messages': {'required': 'Name is required. Please enter valid name for the game.'}},
            'url': {'error_messages': {'required': 'URL is required. Please enter valid URL.'}},
        }
    