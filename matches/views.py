from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import *
from .models import MatchList
from django.db.models.signals import post_save
from django.dispatch import receiver
import itertools
import datetime
import random
venue_lists = ["GMC Stadium", "Tilak Maidan", 'Fatorda', 'Javahar', 'Mohali']

class IndexView(TemplateView):
    template_name = "matches/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        total_teams = Team.objects.all()
        if total_teams.count() < 10:
            context['is_registration'] = True
        else:
            context['is_registration'] = False
            context['match_list'] = MatchList.objects.all()
        # context['is_registration'] = True if (total_teams.count() < 10) else False
        context['team_form'] = TeamForm()
        return context

    def post(self, request, **kwargs):
        team_form = TeamForm(data=request.POST)
        if team_form.is_valid():
            team = team_form.save()
        return redirect('index')


def make_schedule(num_teams, round):
    # combinations = itertools.combinations(list(range(0, num_teams)), 2)/
    # team_list = list(range(1, num_teams + 1))
    team_list = num_teams
    # half = num_teams // 2
    half = 5
    if round:
        team_list = team_list[:1] + team_list[-round:] + team_list[1:-round]

    return {round: list(zip(team_list[:half], team_list[half:] [::-1]))}


@receiver(post_save, sender=Team, dispatch_uid="setting team lineup")
def team_linup(sender, instance, **kwargs):
    total_team_id = Team.objects.values_list('id', flat=True)
    team_list = list(total_team_id)
    if len(team_list) < 10:
        return
    else:
        schedule = [make_schedule(team_list, round) for round in range(10 - 1)]
        schedule_dict = {k: v for x in schedule for k, v in x.items()}
        match_list = []
        start_date = datetime.datetime(2020, 11, 10, 19, 0)
        for key in schedule_dict:
            for items in schedule_dict[key]:
                match_list += [MatchList(team_1_id=items[0], team_2_id=items[1], start_time=start_date,
                                         end_time= start_date + datetime.timedelta(0, 5400), venue=random.choice(venue_lists))]
                start_date += datetime.timedelta(hours=24)
        MatchList.objects.bulk_create(match_list)

