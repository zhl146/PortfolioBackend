from django.http import HttpResponse

from posts.models import Content, Tag


def get_post(request, title_slug):
    query_set = Content.objects.filter(slug=title_slug)
    for item in query_set:
        print(item.content)
    return HttpResponse(query_set[0].content)


def get_post_summary_year(request, year):
    query_set = Content.objects.filter(create_date__year=year)
    return HttpResponse(query_set)


def get_post_summary_month(request, year, month):
    query_set = Content.objects.filter(create_date__year=year,
                                       create_date__month=month)
    return HttpResponse(query_set)


def get_post_summary_day(request, year, month, day):
    query_set = Content.objects.filter(create_date__year=year,
                                       create_date__month=month,
                                       create_date__day=day)
    return HttpResponse(query_set)


def get_post_summaries(request):
    posts_requested = request.GET.get('posts', 5)
    query_set = Content.objects.order_by('-create_date')[posts_requested]
    return HttpResponse(query_set)


def get_post_summaries_by_category(request, category):
    posts_requested = request.GET.get('posts', 5)
    query_set = Content.objects.filter(category=category)[posts_requested]
    return HttpResponse(query_set)


def get_post_summaries_by_tag(request, tag):
    posts_requested = request.GET.get('posts', 5)
    query_set = Tag.objects.filter(tag_desc=tag)[posts_requested]
    return HttpResponse(query_set)
