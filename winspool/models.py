from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    predicted_score = models.FloatField(default=0.0)
    current_score = models.IntegerField(default=0)

    @property
    def teams(self):
        return self.team_set.filter(player=self)

    @property
    def season_score(self):
        score = 0
        for x in self.teams:
            score += x.wins
        return score

    def week_score(self, week):
        score = 0
        for x in self.teams:
            score += x.weekWins(week)
        return score

    def team_week_scores(self, week):
        retval = []
        for t in self.teams:
            retval.append((t.full_name, t.weekWins(week)))
        return retval
        

class Week(models.Model):
    score = models.IntegerField(default=0)
    winning_teams = models.CharField(max_length=11)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    week = models.IntegerField(default=0)
    season = models.IntegerField(default=2018)

class Team(models.Model):
    name = models.CharField(max_length=3)
    full_name = models.CharField(max_length=30)
    pick = models.IntegerField()
    #wins = models.IntegerField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    @property
    def wins(self):
        retwins = 0
        weeks = Week.objects.filter(player=self.player)
        for w in weeks:
            #print("Adding scores for week %d with a score of %d for player %s" % (w.week, w.score, w.player.name))
            if self.name in w.winning_teams.split(','):
                #retwins += w.score
                retwins += 1
        return retwins

    def weekWins(self, weeknum):
        weeks = Week.objects.filter(player=self.player).filter(week=weeknum)
        week = None
        if len(weeks) != 0:
            week = weeks[0]
        else:
            return 0
        if self.name in week.winning_teams.split(","):
            return 1
        else:
            return 0

class NFLGame(models.Model):
    home_team = models.CharField(max_length=3)
    away_team = models.CharField(max_length=3)
    game_id = models.IntegerField()
    complete = models.IntegerField(default=0)
    winner = models.CharField(max_length=3)
    week = models.IntegerField(default=0)
    season = models.IntegerField(default=2018)
