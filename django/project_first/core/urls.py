from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView
from .views import IndexView, FeedView, PostView, CretePostView, EditPostView, like_post, DeletePostView

app_name = 'core'

urlpatterns = [
    url('^posts/$', IndexView.as_view(), name='index'),  # name не обязательно, но желательно
    path('posts/feed/', FeedView.as_view(), name='post-feed'),
    path('posts/create/', CretePostView.as_view(), name='post-create'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', PostView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/edit/', EditPostView.as_view(), name='post-edit'),
    path('posts/<int:post_id>/delete/', DeletePostView.as_view(), name='post-delete'),
    path('posts/<int:post_id>/delete/', TemplateView.as_view(template_name='core/delete_success.html'),
         name='post-delete-success'),
    path('posts/<int:post_id>/like/', like_post, name='post-like'),
]