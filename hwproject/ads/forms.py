from django import forms
from .models import Ad


class ADForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['title', 'description', 'photo']
        labels = {
            'title': 'Заголовок',
            'description': 'Текст объявления',
            'photo': 'Выберите фото'
        }

        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите заголовок'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите текст объявления'}),
            'photo': forms.ClearableFileInput(attrs={'type': 'file', 'class': 'form-control-file'})
        }
