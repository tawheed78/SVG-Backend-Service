from rest_framework import generics, status
from .models import Game
from .serializers import GameSerializer
from rest_framework.response import Response
from .utils import SetPagination
from rest_framework.filters import OrderingFilter
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class GameListAPIView(generics.ListAPIView):
    """
    API endpoint to list and create games.
    """
    queryset  = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = SetPagination
    filter_backends = [OrderingFilter]

    @method_decorator(cache_page(60*2))
    def get(self, *args, **kwargs):
        response = super().get(*args, **kwargs)
        return response


class GameCreateAPIView(generics.CreateAPIView):
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

    @method_decorator(cache_page(60*1))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

        
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

