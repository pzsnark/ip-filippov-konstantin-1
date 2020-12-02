from django.conf.urls import url
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from .views import IndexView, FeedView, PostView, CretePostView, EditPostView, like_post, DeletePostView
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, LogoutView
    )
from .views_auth import LoginView

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
    path('password_reset/', PasswordResetView.as_view(
        success_url=reverse_lazy('core:password-reset-done'),
        template_name='my_auth/password_reset.html'
         ), name='password-reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='my_auth/password_reset_done.html'
    ), name='password-reset-done'),
    path('password_reset/<str:uidb64>/<slug:token>', PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('core:password-reset-complete')
    ), name='password-reset-confirm'),
    path('password_reset/complete', PasswordResetCompleteView.as_view(), name='password-reset-complete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]