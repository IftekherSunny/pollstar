from rest_framework import viewsets
from django.contrib.auth.models import User
from polls.api.serializers.user import UserSerializer

# Create your views here.
class GetUser(viewsets.ModelViewSet):
        queryset = User.objects.all().order_by('-date_joined')
        serializer_class = UserSerializer
