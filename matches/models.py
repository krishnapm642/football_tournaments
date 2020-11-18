from django.db import models



class Team(models.Model):
    name = models.CharField(max_length=100)
    coach = models.CharField(max_length=100, blank=True, null=True)
    manager = models.CharField(max_length=100, blank=True, null=True)
    members = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MatchList(models.Model):
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='first_team')
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='second_team')
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
    is_completed = models.BooleanField(default=False)
    venue = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return '%s ---- %s' % (self.team_1, self.team_2)


class MatchResults(models.Model):
    match = models.ForeignKey(MatchList, on_delete=models.CASCADE)
    goal_scored_team_1 = models.IntegerField(null=True, blank=True, default=0)
    goal_scored_team_2 = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return '%s ---- %s' % (self.match.team_1, self.match.team_2)

