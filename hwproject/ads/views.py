from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Ad
from django.template import loader

# Create your views here.


def index(request):
    last_ad_7 = Ad.objects.all().order_by('-date_pub')
    template = loader.get_template('ads/index.html')
    context = {
        'last_ad_7': last_ad_7,
    }
    return HttpResponse(template.render(context))


def ad_detail(request, ad_id):
    post = get_object_or_404(Ad, id=ad_id)
    # try:
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist as e:
    #     raise Http404('Post with id#{} does not exist'.format(post_id))
    # post = Post.objects.get(id=post_id)
    response = 'Детальное представление поста №{}, описание {}'.format(post.id, post.description)
    return HttpResponse(response)
