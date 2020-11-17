from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post
from django.db.models import Sum
from django.template import loader

# Create your views here.


def index(request):
    popular_posts = Post.objects.annotate(likes_count=Sum('likes')).order_by('-likes_count')
    template = loader.get_template('core/index.html')
    context = {
        'popular_posts': popular_posts,
    }
    return HttpResponse(template.render(context))


def feed(request):
    friends = request.user.profile.friends.all()
    feed_posts = Post.objects.filter(author__in=friends)
    return HttpResponse(feed_posts)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # try:
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist as e:
    #     raise Http404('Post with id#{} does not exist'.format(post_id))
    # post = Post.objects.get(id=post_id)
    response = 'Детальное представление поста №{}, описание {}'.format(post.id, post.description)
    return HttpResponse(response)


def post_edit(request, post_id):
    response = 'Редактирвоание поста №{}'.format(post_id)
    return HttpResponse(response)


def post_create(request):
    response = 'Создание нового поста'
    return HttpResponse(response)


def post_delete(request, post_id):
    response = 'Удаление поста №{}'.format(post_id)
    return HttpResponse(response)


def like_post(request, post_id):
    response = 'Лайкнуть пост №{}'.format(post_id)
    return HttpResponse(response)



