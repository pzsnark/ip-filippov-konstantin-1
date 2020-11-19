from django.conf.urls import url
from django.urls import path
from .views import IndexView, FullListView, ad_detail

app_name = 'ads'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    url(r'(?P<ad_id>[0-9]+)/$', ad_detail, name='ad-detail'),
    path('full_list/', FullListView.as_view(), name='full_view')
]
