from django.http import HttpResponse


def get_post(request, title_slug):
    response = "I should return post named %s"
    return HttpResponse(response % title_slug)


def get_post_summary_year(request, year, num_posts = 5):
    response = "I would return all post summaries in the year {}"
    return HttpResponse(response.format(year))


def get_post_summary_month(request, year, month, num_posts = 5):
    response = "I would return all post summaries in {}/{}"
    return HttpResponse(response.format(month, year))


def get_post_summary_day(request, year, month, day, num_posts = 5):
    response = "I would return all post summaries on {}/{}/{}"
    return HttpResponse(response.format(month, day, year))


def get_post_summaries(request, num_posts = 5):
    return HttpResponse("I should return all post summaries")


def get_post_summaries_by_category(request, category, num_posts = 5):
    response = "I would return all post summaries with category {}"
    return HttpResponse(response.format(category))


def get_post_summaries_by_tag(request, tag, num_posts = 5):
    response = "I would return all post summaries with tag {}"
    return HttpResponse(response.format(tag))
