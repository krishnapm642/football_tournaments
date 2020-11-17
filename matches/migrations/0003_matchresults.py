# Generated by Django 3.1.3 on 2020-11-17 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0002_matchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_scored_team_1', models.IntegerField(blank=True, null=True)),
                ('goal_scored_team_2', models.IntegerField(blank=True, null=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.matchlist')),
            ],
        ),
    ]
