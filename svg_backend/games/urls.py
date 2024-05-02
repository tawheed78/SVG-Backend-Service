from django.urls import path
from .utils import schema_view
from .views import (
    GameRetrieveUpdateAPIView,
    GameDestroyAPIView,
    GameListAPIView,
    GameCreateAPIView
)


urlpatterns = [
    #Endpoint to list all the games and create new game
    path('games', GameListAPIView.as_view()),
    path('games/new-game', GameCreateAPIView.as_view()),

    #Endpoints to retrieve, update and delete a game
    path('games/<int:pk>', GameRetrieveUpdateAPIView.as_view()),
    path('games/<int:pk>', GameRetrieveUpdateAPIView.as_view()),
    path('games/<int:pk>/', GameDestroyAPIView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]