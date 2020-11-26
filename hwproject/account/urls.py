from django.conf.urls import url
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
]
