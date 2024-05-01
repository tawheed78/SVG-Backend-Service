from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    """Admin configuration for the Game model."""
    
    search_fields = ('name', 'author')