# pages/views.py
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer

def home(request: HttpRequest):
    return render(request, "home.html")



@api_view(['GET', 'POST', 'PUT', 'DELETE'])

def game_list(request: HttpRequest):
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            game = serializer.save()
            response_data = {
                'message': 'Game created successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)
