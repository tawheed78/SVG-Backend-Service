from django.urls import path
from .views import (
    GameRetrieveUpdateAPIView,
    GameDestroyAPIView,
    GameListAPIView,
    GameCreateAPIView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="SVG Backend Service",
        default_version='v1',
        description="Game CRUD Operation",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="tawa@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
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