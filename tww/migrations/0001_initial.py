# Generated by Django 2.2.28 on 2022-08-23 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood_text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Writing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writing_text', models.TextField(max_length=400)),
                ('user_name', models.CharField(max_length=20)),
                ('word1', models.CharField(max_length=100)),
                ('word2', models.CharField(max_length=100)),
                ('word3', models.CharField(max_length=100)),
                ('mood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tww.Mood')),
            ],
        ),
    ]
