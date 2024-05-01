from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
    """Serializer for the Game model."""
    class Meta:
        model = Game
        fields = '__all__'
        # extra_kwargs = {
        #     "name": {
        #         "error_messages": {"blank": "Provide a name for the game"}
        #     }
        # }
    
    