from django.http import HttpResponse

# Create your views here.

def get_index(request):
    return HttpResponse('Polls')