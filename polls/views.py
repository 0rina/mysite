# pages/views.py
from django.conf import settings
from django.http import HttpRequest
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Game, User, Rating
from .serializers import GameSerializer, GameNameSerializer
from datetime import timezone
from rest_framework import viewsets


def home(request: HttpRequest):
    return render(request, "home.html")



@api_view(['GET'])
def game_list(request: HttpRequest):
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameNameSerializer(games, many=True)
        request.session['game_list'] = serializer.data  # write data to session
        return Response(serializer.data)

def games_html(request):
    game_names = request.session.get('game_list', [])  # collect date from session
    return render(request, "games1.html", {'game_names': game_names})


@api_view(['POST'])
def save_rating(request):
    if request.method == 'POST':
        serializer = Rating(data=request.data)
        if serializer.is_valid(raise_exception=True):
            game_id = request.data.get('game_id')
            user_id = request.data.get('user_id')
            opinion = request.data.get('opinion')
            mark = request.data.get('mark')

            game = Game.objects.get(id=game_id)
            user = User.objects.get(id=user_id)

            print(game)
            print(user)

            try:
                rating = Rating(game=game, user=user, opinion=opinion, mark=mark, date_field=timezone.now())
                rating.save()
                return Response({"message": "Rating saved successfully"})
            except Exception as e:
                print(e)
                return Response({"message": "Error while saving rating"})


def game_opinion(reqest):
    reqest.session['game_id'] = 2
    reqest.session['user_id']=1
    reqest.session['opinion'] = 'sewfdsa'
    reqest.session['mark']=4

