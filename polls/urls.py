from django.urls import path

from polls import views, connector

urlpatterns = [
    path("home/", views.home),
    path('games/', connector.game_view),
]