import mysql.connector
from django.shortcuts import render
def game_view(request):
    mydb = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="A268@895awq",
        port='3306',
        database='gamesopinion'
    )

    mycursor=mydb.cursor()
    mycursor.execute('SELECT * FROM game')
    games=mycursor.fetchall()
    mycursor.close()
    mydb.close()

    return render(request, 'games.html', {'games': games})