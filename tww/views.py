from multiprocessing import context
from django.http import Http404
from django.shortcuts import render, get_object_or_404
import random

from .models import Mood, Writing


def create(request):
    moods = Mood.objects.all()
    random_index = random.randint(0, len(moods)-1)
    random_mood = moods[random_index].mood_text
    context = {"random_mood": random_mood}
    return render(request, "tww/index.html", context)

def view_all_writings(request):
    writings = Writing.objects.all()
    context = {"writings": writings}
    return render(request, "tww/view-all-writings.html", context)

def view(request, writing_id):
    writing = get_object_or_404(Writing, pk=writing_id)
    context = {"writing": writing}
    return render(request, "tww/view-writing.html", context)
