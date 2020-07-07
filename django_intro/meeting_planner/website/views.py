from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("welcome to the meeting planner" + str(datetime.now()))


def about(request):
    return HttpResponse("heya, im imane and im learning django")

