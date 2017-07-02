from django.http import HttpResponse, JsonResponse
from django.core import serializers
from posts.models import Content, Tag


# gets a single post by querying with title_slug
def get_post(request, title_slug):
    post = Content.objects.get(slug=title_slug)
    json = post.get_client_json()
    return JsonResponse(json)


# gets X number of most recent posts from the requested year
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
# currently returns entire posts and not summaries
def get_post_summary_year(request, year):
    posts_requested = int(request.GET.get('posts', 5))
    post_offset = int(request.GET.get('offset', 0))
    query_set = Content.objects.filter(create_date__year=year).order_by('-create_date')[post_offset:posts_requested]
    json = serializers.serialize('json', query_set)
    return HttpResponse(json)


# gets X number of most recent posts from the requested year/month
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
# currently returns entire posts and not summaries
def get_post_summary_month(request, year, month):
    posts_requested = int(request.GET.get('posts', 5))
    post_offset = int(request.GET.get('offset', 0))
    query_set = Content.objects.filter(create_date__year=year,
                                       create_date__month=month).order_by('-create_date')[post_offset:posts_requested]
    json = serializers.serialize('json', query_set)
    return HttpResponse(json)


# gets X number of most recent posts from the requested year/month/day
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
# currently returns entire posts and not summaries
def get_post_summary_day(request, year, month, day):
    posts_requested = int(request.GET.get('posts', 5))
    post_offset = int(request.GET.get('offset', 0))
    query_set = Content.objects.filter(create_date__year=year,
                                       create_date__month=month,
                                       create_date__day=day)[post_offset:posts_requested]
    json = serializers.serialize('json', query_set)
    return HttpResponse(json)


# gets X number of most recent posts
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
# currently returns entire posts and not summaries
def get_post_summaries(request):
    posts_requested = int(request.GET.get('posts', 5))
    post_offset = int(request.GET.get('offset', 0))
    query_set = Content.objects.order_by('-create_date')[post_offset:posts_requested]
    json = serializers.serialize('json', query_set)
    return HttpResponse(json)


# gets X number of most recent posts with category
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
# currently returns entire posts and not summaries
def get_post_summaries_by_category(request, category):
    posts_requested = int(request.GET.get('posts', 5))
    post_offset = int(request.GET.get('offset', 0))
    query_set = Content.objects.filter(category=category)[post_offset:posts_requested]
    json = serializers.serialize('json', query_set)
    return HttpResponse(json)


# gets X number of most recent posts with tag
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
# currently returns entire posts and not summaries
def get_post_summaries_by_tag(request, tag):
    posts_requested = int(request.GET.get('posts', 5))
    post_offset = int(request.GET.get('offset', 0))
    # gets tags
    tag_set = Tag.objects.filter(tag_desc=tag)
    # uses the tags to cross reference contents
    content_set = Content.objects.filter(tag_list__in=tag_set)[post_offset:posts_requested]
    json = serializers.serialize('json', content_set)
    return HttpResponse(json)
