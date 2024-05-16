# pages/views.py
from django.http import HttpRequest
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer, GameNameSerializer


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
    game_names = request.session.get('game_list', [])  # caollect date from session
    return render(request, "games1.html", {'game_names': game_names})
