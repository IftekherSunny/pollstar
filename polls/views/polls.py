from polls.models import Poll
from django.shortcuts import render, get_object_or_404


def show_polls_list(request):
    ''' Show polls list'''

    polls = Poll.objects.all

    return render(request, 'polls/index.html', {'polls': polls})


def show_vote_page(request, id):
    ''' Show single poll '''

    poll = get_object_or_404(Poll, id=id)

    context = {'poll': poll}

    return render(request, 'polls/vote.html', context)