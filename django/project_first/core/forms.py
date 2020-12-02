from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['description', 'image']
        labels = {
            'description': 'Описание поста',
            'image': 'Выберите картинку'
        }

        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание поста'}),
            'image': forms.ClearableFileInput(attrs={'type': 'file', 'class': 'form-control-file'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']

        widgets = {
            'test': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст комментария'})
        }
