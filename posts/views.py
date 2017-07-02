from django.http import JsonResponse
from posts.models import Content, Tag


# gets a single post by querying with title_slug
def get_post(request, title_slug):
    post = Content.objects.get(slug=title_slug)
    json = post.get_post_json()
    return JsonResponse(json)


# gets X number of most recent posts from the requested year
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
def get_post_summary_year(request, year):
    posts_requested = int(request.GET.get('posts', 5))
    offset_index = int(request.GET.get('offset', 0))
    ending_index = offset_index + posts_requested
    query_set = Content.objects.filter(create_date__year=year).order_by('-create_date')[offset_index:ending_index]
    post_list = {
        'posts': []
    }
    for item in query_set:
        post_list['posts'].append(item.get_summary_json())
    return JsonResponse(post_list)


# gets X number of most recent posts from the requested year/month
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
def get_post_summary_month(request, year, month):
    posts_requested = int(request.GET.get('posts', 5))
    offset_index = int(request.GET.get('offset', 0))
    ending_index = offset_index + posts_requested
    query_set = Content.objects.filter(create_date__year=year,
                                       create_date__month=month).order_by('-create_date')[offset_index:ending_index]
    post_list = {
        'posts': []
    }
    for item in query_set:
        post_list['posts'].append(item.get_summary_json())
    return JsonResponse(post_list)


# gets X number of most recent posts from the requested year/month/day
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
def get_post_summary_day(request, year, month, day):
    posts_requested = int(request.GET.get('posts', 5))
    offset_index = int(request.GET.get('offset', 0))
    ending_index = offset_index + posts_requested
    query_set = Content.objects.filter(create_date__year=year,
                                       create_date__month=month,
                                       create_date__day=day).order_by('-create_date')[offset_index:ending_index]
    post_list = {
        'posts': []
    }
    for item in query_set:
        post_list['posts'].append(item.get_summary_json())
    return JsonResponse(post_list)


# gets X number of most recent posts
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
# currently returns entire posts and not summaries
def get_post_summaries(request):
    posts_requested = int(request.GET.get('posts', 5))
    offset_index = int(request.GET.get('offset', 0))
    ending_index = offset_index + posts_requested
    query_set = Content.objects.order_by('-create_date')[offset_index:ending_index]
    post_list = {
        'posts': []
    }
    for item in query_set:
        post_list['posts'].append(item.get_summary_json())
    return JsonResponse(post_list)


# gets X number of most recent posts with category
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
def get_post_summaries_by_category(request, category):
    posts_requested = int(request.GET.get('posts', 5))
    offset_index = int(request.GET.get('offset', 0))
    ending_index = offset_index + posts_requested
    query_set = Content.objects.filter(category=category).order_by('-create_date')[offset_index:ending_index]
    post_list = {
        'posts': []
    }
    for item in query_set:
        post_list['posts'].append(item.get_summary_json())
    return JsonResponse(post_list)


# gets X number of most recent posts with tag
# X comes from the ?posts param and defaults to 5
# can be offset by Y posts using ?offset= Y
def get_post_summaries_by_tag(request, tag):
    posts_requested = int(request.GET.get('posts', 5))
    offset_index = int(request.GET.get('offset', 0))
    ending_index = offset_index + posts_requested
    # gets tags
    tag_set = Tag.objects.filter(tag_desc=tag)
    # uses the tags to cross reference contents
    content_set = Content.objects.filter(tag_list__in=tag_set).order_by('-create_date')[offset_index:ending_index]
    post_list = {
        'posts': []
    }
    for item in content_set:
        post_list['posts'].append(item.get_summary_json())
    return JsonResponse(post_list)
