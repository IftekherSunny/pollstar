from django.conf.urls import url
from polls.views.polls import PollView, VoteView

urlpatterns = [
    url(r'^$', PollView.as_view(), name="polls"),
    url(r'^(?P<id>[0-9]+)/$', VoteView.as_view(), name="question"),
    url(r'^(?P<id>[0-9]+)/vote$', VoteView.as_view(), name="vote"),
]
