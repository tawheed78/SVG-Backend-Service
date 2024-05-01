from rest_framework import generics, status
from .models import Game
from .serializers import GameSerializer
from rest_framework.response import Response


class GameListCreateAPIView(generics.ListCreateAPIView):
    """
    API endpoint to list and create games.
    """
    queryset  = Game.objects.all()
    serializer_class = GameSerializer


class GameRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    API endpoint to get and update a single game.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

        
class GameDestroyAPIView(generics.DestroyAPIView):
    """
    API endpoint to delete game.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Game deleted successfully."}, status=status.HTTP_200_OK)

