from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render,render_to_response, get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth.decorators import login_required
from winspool.models import Player

# Create your views here.
def index(request):
    return render(request, 'winspool/index.html', {})

@login_required
def summary(request):
    retval = []
    players = Player.objects.all()
    for p in players:
        tmpdict = {"player": p}
        teams = p.teams
        tmpdict["team_1"] = teams[0]
        tmpdict["team_2"] = teams[1]
        tmpdict["team_3"] = teams[2]
        retval.append(tmpdict)
    return render(request, 'winspool/summary.html', {"results": retval})

@login_required
def details(request):
    retval = []
    players = Player.objects.all()
    for p in players:
        tmpdict = {"player": p}
        teams = p.teams
        tmpdict["team_1"] = teams[0]
        tmpdict["team_2"] = teams[1]
        tmpdict["team_3"] = teams[2]
        for x in range(17):
            for y in range(3):
                weekwins = teams[y].weekWins(x+1)
                tmpdict["week_%d_%d" % (x+1,y+1)] = weekwins
        retval.append(tmpdict)
    return render(request, 'winspool/summary_details.html', {"results": retval})


