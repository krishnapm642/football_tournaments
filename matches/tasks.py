from football_tournaments.celery import app
from .models import MatchList, MatchResults
from datetime import datetime
from django.utils import timezone


@app.task
def check_match_status():
    current_time = datetime.now(tz=timezone.utc)
    try:
        match_list = MatchList.objects.filter(end_time__lte=current_time, is_completed=False)
        if match_list:
            for items in match_list:
                items.is_completed = True
                items.save()
                print("this is savinggg")
                obj = MatchResults(match=items)
                obj.save()
    except:
        pass
    return
