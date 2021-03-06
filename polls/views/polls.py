from polls.models import Poll
from polls.models import Choice
from polls.models import Question
from django.contrib import messages
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class PollView(View):
    """
    Poll view
    """

    def get(self, request):
        """
        Show polls list
        """

        polls = Poll.objects.all()
        paginator = Paginator(polls, 10)

        page = request.GET.get('page')

        try:
            polls = paginator.page(page)
        except PageNotAnInteger:
            polls = paginator.page(1)
        except EmptyPage:
            polls = paginator.page(paginator.num_pages)

        return render(request, 'index.html', {'polls': polls})


class VoteView(View):
    """
    Vote view
    """

    def get(self, request, id):
        """
        Show single poll
        """

        poll = get_object_or_404(Poll, id=id)

        context = {'poll': poll, 'id': id}

        return render(request, 'vote.html', context)


    def post(self, request, id):
        """
        Accept vote from voter
        """

        # count and store new voter
        for data in request.POST:
            if data != 'csrfmiddlewaretoken':
                totalvoter = Question.objects \
                                 .get(id=data) \
                                 .total_voter + 1

                Question.objects.filter(id=data) \
                    .update(total_voter=totalvoter)

        # Count and store up vote's for the all selected choice
        for data in request.POST:
            if data != 'csrfmiddlewaretoken':
                upvote = Choice.objects \
                             .get(id=request.POST[data]) \
                             .total_vote + 1

                Choice.objects \
                    .filter(id=request.POST[data]) \
                    .update(total_vote=upvote)

        messages.success(request, 'Your vote successfully submitted')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))