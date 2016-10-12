from django.conf.urls import url, include
from rest_framework import routers
from polls.api.views.polls import GetUser

router = routers.DefaultRouter()

# register routes
router.register(r'^', GetUser)


urlpatterns = [
    url(r'^', include(router.urls)),
]
