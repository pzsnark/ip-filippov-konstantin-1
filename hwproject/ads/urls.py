from django.conf.urls import url
from django.urls import path
from .views import IndexView, FullListView, AdDetail, ad_favor, ad_create, ad_remove

app_name = 'ads'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    url(r'(?P<ad_id>[0-9]+)/$', AdDetail.as_view(), name='ad_detail'),
    path('full_list/', FullListView.as_view(), name='full_list'),
    path('<int:ad_id>/ad_favor/', ad_favor, name='ad_favor'),
    path('<int:ad_id>/ad_remove/', ad_remove, name='ad_remove'),
    path('ad_create/', ad_create, name='ad_create'),
]
