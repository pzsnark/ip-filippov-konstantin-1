from django.conf.urls import url
from django.urls import path
from .views import IndexView, FeedView, post_detail, post_create, post_edit, like_post, post_delete

app_name = 'core'

urlpatterns = [
    url('^posts/$', IndexView.as_view(), name='index'),  # name не обязательно, но желательно
    path('posts/feed/', FeedView.as_view(), name='post-feed'),
    path('posts/create/', post_create, name='post-create'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', post_detail, name='post-detail'),
    path('posts/<int:post_id>/edit/', post_edit, name='post-edit'),
    path('posts/<int:post_id>/delete/', post_delete, name='post-delete'),
    path('posts/<int:post_id>/like/', like_post, name='post-like'),
]