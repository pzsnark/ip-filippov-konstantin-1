from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    birth_time = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='users/avatars', default='users/default.png')

    def __str__(self):
        return str(self.user.username)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return '{1} '.format(self.id, self.name)


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.TextField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=False, blank=False)
    photo = models.ImageField(upload_to='users/ad_photos', blank=True)
    date_pub = models.DateTimeField(default=timezone.now)
    date_up = models.DateTimeField(null=True, blank=True)
    favorite = models.ManyToManyField(User, related_name='favorite', blank=True)
    categories = models.ManyToManyField(Category, related_name='category', blank=True)

    def __str__(self):
        return 'Объявление #{0}, автор - {1} '.format(self.id, self.author.username)

    @property
    def short_text(self):
        return self.description[:25]
