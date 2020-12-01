from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from .models import Post, Comment
from django.views.generic import ListView, View, CreateView, DeleteView, DetailView, UpdateView
from django.db.models import Sum
from django.template import loader
from .forms import PostForm, CommentForm


# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'core/index.html'
    context_object_name = 'popular_posts'

    def get_queryset(self):
        return self.model.objects.annotate(likes_count=Sum('likes')).order_by('-likes_count')


class PostView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'
    pk_url_kwarg = 'post_id'
    comment_form = CommentForm

    def get(self, request, post_id, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['comments'] = Comment.objects.filter(in_post__id=post_id).order_by('-date_pub')
        if request.user.is_authenticated:
            context['comment_form'] = self.comment_form
        return self.render_to_response(context)

    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post, id=post_id)
        form = self.comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.in_post = post
            comment.save()
            return render(request, self.template_name, context={
                'comment_form': self.comment_form,
                'post': post,
                'comments': Comment.objects.filter(in_post__id=post_id).order_by('-date_pub')
            })
        else:
            return render(request, self.template_name, context={
                'comment_form': form,
                'post': post,
                'comments': Comment.objects.filter(in_post__id=post_id).order_by('-date_pub')
            })


class EditPostView(UpdateView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'core/post_edit.html'
    form_class = PostForm

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse('core:post-detail', args=(post_id, ))

    def get(self, request, post_id, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author != request.user:
            raise Http404()
        return super().get(self, request, post_id, args, kwargs)


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


class CretePostView(CreateView):
    form_class = PostForm
    template_name = 'core/post_create.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        context = {}
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            context['form'] = self.form_class
            context['post_was_created'] = True
            return render(request, self.template_name, context)
        else:
            context['post_was_created'] = False
            context['form'] = form
        return render(request, self.template_name, context)


class DeletePostView(DeleteView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'core/post_delete.html'

    def get_success_url(self):
        post_id = self.kwargs['post_id']
        return reverse('core:post-delete-success', args=(post_id, ))

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


# def post_create(request):
#     form = PostForm()
#     context = {
#         'form': PostForm()
#     }
#     if request.method == 'GET':
#         return render(request, 'core/post_create.html', context)
#     elif request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             return redirect('/posts/', request)
#         else:
#             context = {
#                 'form': form
#             }
#             return render(request, 'core/post_create.html', context)


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
