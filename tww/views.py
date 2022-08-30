from multiprocessing import context
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
import random

from .models import Mood, Writing


def create(request):
    moods = Mood.objects.all()
    random_index = random.randint(0, len(moods) - 1)
    random_mood = moods[random_index].mood_text
    context = {"random_index": random_index, "random_mood": random_mood}
    return render(request, "tww/create.html", context)


def upload(request, random_index):
    moods = Mood.objects.all()
    w = Writing(
        writing_text=request.POST.get("writing-text"),
        user_name=request.POST.get("user-name"),
        word1="坊主",
        word2="屏風",
        word3="上手",
        mood=moods[random_index],
    )
    w.save()
    writing_id = w.id
    return HttpResponseRedirect(reverse("tww:view", args=(writing_id,)))


def view_all_writings(request):
    writings = Writing.objects.all()
    context = {"writings": writings}
    return render(request, "tww/view-all-writings.html", context)


def view(request, writing_id):
    writing = get_object_or_404(Writing, pk=writing_id)
    context = {"writing": writing}
    return render(request, "tww/view-writing.html", context)
