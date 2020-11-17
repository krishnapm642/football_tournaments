from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from matches.models import MatchResults

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('account:home')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'account/login.html', {})


class Home(View):

    def get(self, request, *args, **kwargs):
        match_result_list = MatchResults.objects.filter()
        return render(request, 'account/home.html', {'match_result_list': match_result_list})


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')