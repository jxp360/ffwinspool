#!/usr/bin/env python
import os, time, sys
import psycopg2
sys.path.append("../")
os.environ['DJANGO_SETTINGS_MODULE'] = 'ffwinspool.settings';
import django
django.setup()
from winspool.models import Player, Week, Team, NFLGame
from django.db.models import Q

def getGames(db, week=None, season=2018):
    cur = db.cursor()
    if not week is None:
        search_str = "select gamekey, home_team, away_team, finished, home_score, away_score, week, season_year from game where week=%d AND season_type='Regular' AND season_year=%d" % (week, season)
    else:
        search_str = "select gamekey, home_team, away_team, finished, home_score, away_score, week, season_year from game where season_type='Regular' AND season_year=%d" %  (season)
    cur.execute(search_str)
    games = cur.fetchall()
    return games

def updateGame(gid, hteam, ateam, finished, hscore, ascore, week, season):
    update=False
    try:
        game = NFLGame.objects.get(game_id=gid)
        print("Found game; checking if it is complete")
    except: #winspool.models.DoesNotExist:
        print("Did not find game; adding to db")
        update = True
        game = NFLGame()
        game.game_id = int(gid)
        game.home_team = hteam
        game.away_team = ateam
        print("Setting game for week %d in season %d" % (week, season))
        game.week = week
        game.year = season
    if game.complete != finished:
        print("Updating completion of game: %s vs %s" % (game.home_team, game.away_team))
        update = True
        game.complete = finished
        if hscore < ascore:
            game.winner = game.away_team
        elif ascore < hscore:
            game.winner = game.home_team
        else:
            print("Game ended in tie; no points awarded")
    if update:
        game.save()
    
def updatePlayerWeek(db, player=None, week=None, season=2018):
    #If week == None, do all
    weeks = [week]
    if player is None:
        players = Player.objects.all()    
    else:
        players = Player.objects.get(player)
    if week is None:
        weeks = range(17)
    for weeknum in weeks:
        #Go get all games for week
        games = getGames(db, weeknum)
        for g in games:
            updateGame(int(g[0]), g[1], g[2], g[3], g[4], g[5], g[6], g[7])
        #Check scores for player
        completed_games = NFLGame.objects.filter(season=season, week=weeknum, complete=True)
        for p in players:
            teams = Team.objects.filter(player=p)
            if teams.count() != 3:
                print("Error: Player %s does not have 3 teams; they have %d" % (p.name, teams.count()))
            completed_games = NFLGame.objects.filter(week=weeknum,season=season, complete=True).filter(Q(winner=teams[0].name)|Q(winner=teams[1].name)|Q(winner=teams[2].name))
            try:
                ws = Week.objects.get(player=p, week=weeknum, season=season)
            except:
                ws = Week()
                ws.player = p
                ws.week = weeknum
                ws.season = season 
            ws.score = completed_games.count()
            winning_teams = []
            for cg in completed_games:
                winning_teams.append(cg.winner)
            ws.winning_teams = ','.join(winning_teams)
            ws.save()

    #Update Scores
    for p in players:
        weeks = Week.objects.filter(player=p)
        total_score = 0
        for w in weeks:
            total_score += w.score
        p.current_score = total_score
        p.save()

if __name__ == "__main__":

    nfldb = "threeandout.cjftsjpuovni.us-east-1.rds.amazonaws.com"
    db = psycopg2.connect(host=nfldb, database="nfldb", user="nfldb", password="Thr33&0ut!") 
    NFLGame.objects.all().delete()
    updatePlayerWeek(db, None, None, 2018)

    total_weeks = 3
    #Update Scores
    for p in Player.objects.all():
        print("Total score for %s is %d" % (p.name, p.current_score))
        print("Total score for %s is %d" % (p.name, p.season_score))
        for wx in range(total_weeks):
            x = wx+1
            print("Score for week %d is %d for player %s" % (x, p.week_score(x), p.name))
            ts = p.team_week_scores(x)
            for y in range(len(ts)):
                print ("Team %d: %s Week: %d Score: %d" % (y, ts[y][0], x, ts[y][1]))

