from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Post
from django.views.generic import ListView, View
from django.db.models import Sum
from django.template import loader
from .forms import PostForm


# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'popular_posts'

    def get_queryset(self):
        return self.model.objects.annotate(likes_count=Sum('likes')).order_by('-likes_count')


# def index(request):
#     popular_posts = Post.objects.annotate(likes_count=Sum('likes')).order_by('-likes_count')
#     template = loader.get_template('core/index.html')
#     context = {
#         'popular_posts': popular_posts,
#     }
#     return render(request, 'core/index.html', context)


class FeedView(View):
    template_name = 'core/feed.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            friends = request.user.user_profile.friends.all()
            feed_posts = Post.objects.filter(author__in=friends)
            context = {
                'feed_posts': feed_posts
            }
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name)


# def feed(request):
#     friends = request.user.profile.friends.all()
#     feed_posts = Post.objects.filter(author__in=friends)
#     return HttpResponse(feed_posts)


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
    form = PostForm()
    context = {
        'form': PostForm()
    }
    if request.method == 'GET':
        return render(request, 'core/post_create.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/posts/', request)
        else:
            context = {
                'form': form
            }
            return render(request, 'core/post_create.html', context)


def post_delete(request, post_id):
    response = 'Удаление поста №{}'.format(post_id)
    return HttpResponse(response)


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        post.save()
    return redirect(request.META.get('HTTP_REFERER'), request)  # возвращаем пользователя назад
