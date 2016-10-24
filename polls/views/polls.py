from polls.models import Poll
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from polls.models import Choice
from polls.models import Question


def show_polls_list(request):
    ''' Show polls list'''

    polls = Poll.objects.all

    return render(request, 'index.html', {'polls': polls})


def show_vote_page(request, id):
    ''' Show single poll '''

    poll = get_object_or_404(Poll, id=id)

    context = {'poll': poll, 'id': id}

    return render(request, 'vote.html', context)


def accept_vote(request, id):
    ''' Accept vote from voter '''

    # count and store new voter
    for data in request.POST:
        if data != 'csrfmiddlewaretoken':

            totalvoter = Question.objects\
                             .get( id = data )\
                             .total_voter + 1

            Question.objects.filter( id = data )\
                .update( total_voter = totalvoter )

    # Count and store up vote's for the all selected choice
    for data in request.POST:
        if data != 'csrfmiddlewaretoken':

            upvote = Choice.objects\
                         .get( id=request.POST[data] )\
                         .total_vote + 1

            Choice.objects\
                .filter( id=request.POST[data] )\
                .update( total_vote= upvote )

    return HttpResponse('done')
