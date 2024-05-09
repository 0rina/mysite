# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    genre = models.ForeignKey('Genre', models.DO_NOTHING, blank=True, null=True)
    game_name = models.CharField(max_length=256, blank=True, null=True)
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game'


class GamePlatform(models.Model):
    game_platform_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    platform = models.ForeignKey('Platform', models.DO_NOTHING)
    release_year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_platform'


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class Platform(models.Model):
    platform_id = models.AutoField(primary_key=True)
    platform_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'platform'


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publisher'


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    opinion = models.CharField(max_length=1024, blank=True, null=True)
    mark = models.IntegerField(blank=True, null=True)
    date_field = models.DateField(db_column='date_', blank=True, null=True)  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'rating'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    nick = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
