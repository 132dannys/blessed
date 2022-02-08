from .models import Post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'anons', 'text', 'published_date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "published_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
        }
