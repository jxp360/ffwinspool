#!/usr/bin/env

import os, time, sys
sys.path.append("..")
os.environ['DJANGO_SETTINGS_MODULE'] = 'ffwinspool.settings';
import django
django.setup()
from winspool.models import Player, Team

teams1 = {'ARI': 'Arizona Cardinals',
          'ATL': 'Atlanta Falcons',
          'BAL': 'Baltimore Ravens',
          'BUF': 'Buffalo Bills',
          'CAR': 'Carolina Panthers',
          'CHI': 'Chicago Bears',
          'CIN': 'Cincinnati Bengals',
          'CLE': 'Cleveland Browns',
          'DAL': 'Dallas Cowboys',
          'DEN': 'Denver Broncos',
          'DET': 'Detroit Lions',
          'GB': 'Green Bay Packers',
          'HOU': 'Houston Texans',
          'IND': 'Indianapolis Colts',
          'JAC': 'Jacksonville Jaguars',
          'KC': 'Kansas City Chiefs', 
          'MIA': 'Miami Dolphins',
          'MIN': 'Minnesota Vikings',
          'NE': 'New England Patriots', 
          'NO': 'New Orleans Saints', 
          'NYG': 'New York Giants', 
          'NYJ': 'New York Jets', 
          'OAK': 'Oakland Raiders',
          'PHI': 'Philadelphia Eagles',
          'PIT': 'Pittsburgh Steelers',
          'SD': 'San Diego Chargers',
          'SEA': 'Seattle Seahawks',
          'SF': 'San Francisco 49ers',
          'STL': 'St. Louis Rams',
          'TB': 'Tampa Bay Buccaneers',
          'TEN': 'Tennessee Titans',
          'WAS': 'Washington Redskins',
          'LA': 'Los Angeles Rams',
          'LAC': 'Los Angeles Chargers'
          }



if __name__ == "__main__":

    players = [("Jake Christie", "", "NE", "CIN", "NYG", 1, 20, 26),
               ("Jeff Pfeiffenberger", "", "PHI", "BAL", "TB", 2, 16, 29),
               ("Rich Christie", "", "PIT", "KC", "NYJ", 3, 13, 30),
               ("Rich Christie, Jr", "", "GB", "DEN", "ARI", 4, 18, 25),
               ("Bill Christie III", "", "LA", "TEN", "WAS", 5, 15, 27),
               ("Nick Christie", "", "MIN", "OAK", "IND", 6, 19, 22),
               ("Bill Christie, Jr", "", "ATL", "HOU", "MIA", 7, 11, 28),
               ("Steve Christie", "", "NO", "DAL", "SEA", 8, 17, 21),
               ("Alex Tamburino", "", "LAC", "SF", "CHI", 9, 14, 23),
               ("Craig Miller", "", "JAC", "CAR", "DET", 10, 12, 24)]

    overwrite = False
    clean_slate = True

    if clean_slate:
        print("Deleting all objects from Player database")
        Player.objects.all().delete()    

    for p in players:
        try:
            plr = Player.objects.get(name=p[0])
            print("Found player %s" % plr.name)
        except: #winspool.models.DoesNotExist:
            print("Did not find player %s; adding to db" % p[0])
            plr = Player()
            plr.name = p[0]
            plr.email = p[1]
            plr.save()
            team1 = Team()
            team1.player = plr
            team1.name = p[2]
            team1.full_name = teams1[p[2]]
            team1.pick = p[5]
            team1.save()
            team2 = Team()
            team2.player = plr
            team2.name = p[3]
            team2.full_name = teams1[p[3]]
            team2.pick = p[6]
            team2.save()
            team3 = Team()
            team3.player = plr
            team3.name = p[4]
            team3.full_name = teams1[p[4]]
            team3.pick = p[7]
            team3.save()


