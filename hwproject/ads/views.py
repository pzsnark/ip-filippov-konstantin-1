from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Ad, Category
from django.views.generic import ListView, View
from django.template import loader

# Create your views here.


class IndexView(ListView):
    model = Ad
    template_name = 'ads/index.html'
    context_object_name = 'last_ad'

    def get_queryset(self):
        last_ad = self.model.objects.all().order_by('-date_pub')
        last_ad_count = 7
        return last_ad[:last_ad_count]


class FullListView(ListView):
    model = Ad
    template_name = 'ads/full_list.html'
    context_object_name = 'full_list'

    def get_queryset(self):
        full_list = self.model.objects.all().order_by('-date_pub')
        return full_list


# def index(request):
#     last_ad_7 = Ad.objects.all().order_by('-date_pub')
#     template = loader.get_template('ads/index.html')
#     context = {
#         'last_ad_7': last_ad_7,
#     }
#     return HttpResponse(template.render(context))


def ad_detail(request, ad_id):
    post = get_object_or_404(Ad, id=ad_id)
    # try:
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist as e:
    #     raise Http404('Post with id#{} does not exist'.format(post_id))
    # post = Post.objects.get(id=post_id)
    response = 'Детальное представление поста №{}, описание {}'.format(post.id, post.description)
    return HttpResponse(response)
