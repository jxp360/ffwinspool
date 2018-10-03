from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render,render_to_response,RequestContext, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'winspool/index.html', {})

@login_required
def summary(request):
    weeks = range(1,18)
    return render(request, 'winspool/summary.html', {"weeks":weeks})


