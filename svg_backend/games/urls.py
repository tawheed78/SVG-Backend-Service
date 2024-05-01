from django.urls import path
from .views import (
    GameRetrieveUpdateAPIView,
    GameDestroyAPIView,
    GameListCreateAPIView
)

urlpatterns = [
    #Endpoint to list all the games and create new game
    path('', GameListCreateAPIView.as_view()),
    path('create-game/', GameListCreateAPIView.as_view()),

    #Endpoints to retrieve, update and delete a game
    path('<int:pk>/game/', GameRetrieveUpdateAPIView.as_view()),
    path('<int:pk>/update-game/', GameRetrieveUpdateAPIView.as_view()),
    path('<int:pk>/delete-game/', GameDestroyAPIView.as_view()),
]