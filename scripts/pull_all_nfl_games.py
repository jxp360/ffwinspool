#!/usr/bin/env python
import os, time, sys
import psycopg2
sys.path.append("../")
os.environ['DJANGO_SETTINGS_MODULE'] = 'ffwinspool.settings';
import django
django.setup()
from winspool.models import NFLGame

def getGames(db, week=None, season=2018):
    cur = db.cursor()
    if not week is None:
        search_str = "select gamekey, home_team, away_team, finished, home_score, away_score from game where week=%d AND season_type='Regular' AND season_year=%d" % (week, season)
    else:
        search_str = "select gamekey, home_team, away_team, finished, home_score, away_score from game where season_type='Regular' AND season_year=%d" %  (season)
    cur.execute(search_str)
    games = cur.fetchall()
    return games

def updateGame(gid, hteam, ateam, finished, hscore, ascore):
    update = False
    try:
        game = NFLGame.objects.get(game_id=gid)
        print("Found game; checking if it is complete")
    except: #winspool.models.DoesNotExist:
        print("Did not find game; adding to db")
        update = True
        game = NFLGame()
        game.game_id = int(g[0])
        game.home_team = g[1]
        game.away_team = g[2]

    if game.complete != g[3]:
        print("Updating completion of game: %s vs %s" % (game.home_team, game.away_team))
        update = True
        game.complete = g[3]
        if g[4] < g[5]:
            game.winner = game.home_team
        else:
            game.winner = game.away_team
    
    if update:
        game.save()
    
    
if __name__ == "__main__":

    nfldb = "threeandout.cjftsjpuovni.us-east-1.rds.amazonaws.com"
    db = psycopg2.connect(host=nfldb, database="nfldb", user="nfldb", password="Thr33&0ut!") 
    games = getGames(db)
    for g in games:
        print(g)
        updateGame(int(g[0]), g[1], g[2], g[3], g[4], g[5])
