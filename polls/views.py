# pages/views.py
from django.http import HttpRequest
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game, Genre, Platform
from .serializers import GameSerializer, GameNameSerializer, GenreSerializer, PlatformSerializer


def home(request: HttpRequest):
    return render(request, "home.html")


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def game_list(request: HttpRequest):
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameNameSerializer(games, many=True)
        request.session['game_list'] = serializer.data  # write data to session
        return Response(serializer.data)

def games_html(request):
    game_names = request.session.get('game_list', [])  # collect date from session
    return render(request, "games1.html", {'game_names': game_names})

@api_view(['GET'])
def genre_list(request: HttpRequest):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        request.session['genre_list'] = serializer.data  # write data to session
        return Response(serializer.data)

def genre_html(request):
    genre_names = request.session.get('genre_list', [])
    return render(request, "home.html", {'genre_names': genre_names})

@api_view(['GET'])
def platform_list(request: HttpRequest):
    if request.method == 'GET':
        platforms = Platform.objects.all()
        serializer = PlatformSerializer(platforms, many=True)
        request.session['platform_list'] = serializer.data  # write data to session
        return Response(serializer.data)

def platform_html(request):
    platforms = request.session.get('platform_list', [])
    return render(request, "games.html", {'platforms': platforms})
