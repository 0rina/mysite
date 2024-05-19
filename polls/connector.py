import mysql.connector
from django.shortcuts import render
def game_view(request):
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="mama21",
        port='3306',
        database='game_rating'
    )

    mycursor=mydb.cursor()
    mycursor.execute('SELECT game_name FROM game')
    games=mycursor.fetchall()
    mycursor.close()
    mydb.close()

    return render(request, 'games.html', {'games': games})