from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from polls import views, connector
urlpatterns = [
    path('', views.home),
    path("admin/", admin.site.urls),
    path("polls/", views.home),
    path("games/", connector.game_view),
    path("g1/", views.game_list),

]
