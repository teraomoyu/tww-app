from django.db import models

# Create your models here.
class Mood(models.Model):
    mood_text = models.CharField(max_length=100)

    def __str__(self):
        return self.mood_text

class Writing(models.Model):
    writing_text = models.TextField(max_length=400)
    user_name = models.CharField(max_length=20)
    word1 = models.CharField(max_length=100)
    word2 = models.CharField(max_length=100)
    word3 = models.CharField(max_length=100)
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE)

    def __str__(self):
        return self.writing_text
