from django.conf.urls import url, include
from .views import polls

urlpatterns = [
    url(r'^$', polls.show_polls_list),
    url(r'^(?P<id>[0-9]+)/$', polls.show_vote_page),
    url(r'^(?P<id>[0-9]+)/vote$', polls.accept_vote, name="vote"),
]
