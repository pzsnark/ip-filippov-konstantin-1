from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Ad, Category
from django.views.generic import ListView, View, DetailView
from django.template import loader
from .forms import ADForm
from django.utils import timezone
from django.contrib.auth import login, logout


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
        context.update({'button_fav': "в избранном" if self.request.user in ad.favorite.all() else "добавить в избранное"})
        context.update({'button_rm': '' if self.request.user == ad.author else 'hidden'})
        return context


@login_required
def ad_favor(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.method == 'POST':
        if request.user in ad.favorite.all():
            ad.favorite.remove(request.user)
        else:
            ad.favorite.add(request.user)
            ad.save()
        return redirect(request.META.get('HTTP_REFERER'), request)  # возвращаем пользователя назад
    else:
        return redirect('ads:ad_detail', ad_id=ad.id)


@login_required
def ad_create(request):
    template_name = 'ads/ad_create.html'
    context = {'form': ADForm()}
    if request.method == 'GET':
        return render(request, template_name, context)
    elif request.method == 'POST':
        form = ADForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.date_pub = timezone.now()
            ad.author = request.user
            ad.save()
            context['ad_create_result'] = 'Объявление создано'
            return redirect('ads:ad_detail', ad_id=ad.id)
        else:
            context['ad_create_result'] = 'Объявление не создано'
            context['form'] = form
            return render(request, template_name, context)


def ad_edit(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    if request.method == 'POST':
        form = ADForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.date_pub = timezone.now()
            ad.save()
            return redirect('ad_detail', id=ad_id)
    else:
        form = ADForm(instance=ad)
    return render(request, 'ads/ad_edit.html', {'form': form})


def ad_remove(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    context = {'ad_remove_result': 'Невозможно удалить'}
    if request.method == 'POST':
        if request.user.is_staff == 1:
            Ad.objects.filter(id=ad_id).delete()
            return HttpResponse('Объявление удалено')
        elif request.user == ad.author:
            Ad.objects.filter(id=ad_id).delete()
            return HttpResponse('Объявление удалено')
        else:
            return render(request, 'ads/ad_detail.html', context)

