from django.http import HttpResponse


def get_post(request, title_slug):
    response = "I should return post named %s"
    return HttpResponse(response % title_slug)


def get_post_summary_year(request, year):
    posts_requested = request.GET.get('posts', 5)
    response = "I would return all post summaries in the year {}"
    return HttpResponse(response.format(year))


def get_post_summary_month(request, year, month):
    posts_requested = request.GET.get('posts', 5)
    response = "I would return all post summaries in {}/{}"
    return HttpResponse(response.format(month, year))


def get_post_summary_day(request, year, month, day):
    posts_requested = request.GET.get('posts', 5)
    response = "I would return all post summaries on {}/{}/{}"
    return HttpResponse(response.format(month, day, year))


def get_post_summaries(request):
    posts_requested = request.GET.get('posts', 5)
    response = "I would return the latest {} post summaries"
    return HttpResponse(response.format(posts_requested))


def get_post_summaries_by_category(request, category):
    posts_requested = request.GET.get('posts', 5)
    response = "I would return all post summaries with category {}"
    return HttpResponse(response.format(category))


def get_post_summaries_by_tag(request, tag):
    posts_requested = request.GET.get('posts', 5)
    response = "I would return all post summaries with tag {}"
    return HttpResponse(response.format(tag))
