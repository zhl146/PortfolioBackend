from django.http import HttpResponse


def index(request):
    return HttpResponse("I should return a blog post")
