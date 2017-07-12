from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<year>[\d]{4})/?$',
        views.get_post_summary_year,
        name='get_post_summary_year'
    ),
    url(
        r'^(?P<year>[\d]{4})/(?P<month>[\d]{2})/?$',
        views.get_post_summary_month,
        name='get_post_summary_month'
    ),
    url(
        r'^(?P<year>[\d]{4})/(?P<month>[\d]{2})/(?P<day>[\d]{2})/?$',
        views.get_post_summary_day,
        name='get_post_summary_day'
    ),
    url(
        r'^(?P<title_slug>[-\w]+)/?$',
        views.get_post,
        name='get_post'
    ),
    url(
        r'^category/(?P<category>[-\w]+)/?$',
        views.get_post_summaries_by_category,
        name='get_post_summaries_by_category'
    ),
    url(
        r'^tag/(?P<tag>[-\w]+)/?$',
        views.get_post_summaries_by_tag,
        name='get_post_summaries_by_tag'
    ),
    url(
        r'',
        views.get_post_summaries,
        name='get_post_summaries'
    ),
]
