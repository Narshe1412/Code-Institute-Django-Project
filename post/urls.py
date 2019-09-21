from django.conf.urls import url
from .views import get_all_posts, post_detail, show_post_form, get_news, get_blogs

urlpatterns = [
    url(r'^$', get_news, name="get_news"),
    url(r'^blog/$', get_blogs, name="get_blogs"),
    url(r'^all/$', get_all_posts, name="get_all_posts"),
    url(r'^(?P<pk>\d+)/$', post_detail, name="post_detail"),
    url(r'^new/$', show_post_form, name="new_post"),
    url(r'^(?P<pk>\d+)/edit/$', show_post_form, name="edit_post")
    ]