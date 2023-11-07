
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hey There!!!')


def about(request):
    return HttpResponse('About Page!!!')