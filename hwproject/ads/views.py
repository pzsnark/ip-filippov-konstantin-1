from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Ad, Category
from django.views.generic import ListView, View, DetailView
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


# def ad_detail(request, ad_id):
#     detail = get_object_or_404(Ad, id=ad_id)
#     template = loader.get_template('ads/ad_detail.html')
#     context = {
#         'detail': detail
#     }
#     return HttpResponse(template.render(context, request))


class AdDetail(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    context_object_name = 'ad_detail'
    pk_url_kwarg = 'ad_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ad = self.get_object()
        context.update({'button_fav': "добавить в избранное" if self.request.user in ad.favorite.all() else "в избранном"})
        return context


# сделать проверку на метод POST
def ad_favor(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.user in ad.favorite.all():
        ad.favorite.remove(request.user)
    else:
        ad.favorite.add(request.user)
        ad.save()
    return redirect(request.META.get('HTTP_REFERER'), request)  # возвращаем пользователя назад






