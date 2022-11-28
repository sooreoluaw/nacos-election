from urllib import response
from django.http import HttpRequest, HttpResponseBadRequest
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from vote.forms import VoterLoginForm
from vote.models import Nominee, Poll, Voter

# Create your views here.


@require_http_methods(["GET", "POST"])
def login(request: HttpRequest):
    matric = None
    form = VoterLoginForm()
    if request.method == "POST":
        form = VoterLoginForm(request.POST)
    if form.is_valid():
        matric = form.cleaned_data['matric']
    else:
        return render(request, "login.html", {"form": form})

    response = redirect('vote:vote')
    response.set_cookie('matric_no', matric)
    return response


@require_http_methods(["POST"])
def logout(request: HttpRequest):
    response = redirect('vote:login')
    response.delete_cookie('matric_no')
    return response


@require_http_methods(["POST", "GET"])
def vote(request: HttpRequest):
    if 'matric_no' not in request.COOKIES:
        return redirect('vote:login')
    voter = get_object_or_404(
        Voter, identifier=request.COOKIES.get('matric_no'))
    if voter.has_voted:
        raise HttpResponseBadRequest('Double voting not allowed')
    polls = get_list_or_404(Poll)
    if request.method == "GET":
        return render(request, 'vote.html', {'polls': polls, 'voter': voter})
    else:
        for poll in polls:
            choice = request.POST.get(f"poll_{poll.id}")
            nominee = get_object_or_404(Nominee, pk=choice)
            nominee.votes += 1
            nominee.save()
            voter.has_voted = True

        return redirect('vote:success')


@require_http_methods(["GET"])
def success(request: HttpRequest):
    return render(request, 'successful.html')
