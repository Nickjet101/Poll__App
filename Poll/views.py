from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Obidient. You're at COHORT-1 polls index.")