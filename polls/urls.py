from django.conf.urls import url, include
from .views import polls

urlpatterns = [
    url(r'^', polls.get_index),
]
