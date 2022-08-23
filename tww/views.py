from django.shortcuts import render
from django.http import HttpResponse
from .models import Mood
import random


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def create(request):
    moods = Mood.objects.all()
    random_index = random.randint(0, len(moods)-1)
    random_mood = moods[random_index].mood_text
    return HttpResponse(f"キーワードは「単語１」，「単語２」，「単語３」です．{random_mood}雰囲気で書きましょう．")
