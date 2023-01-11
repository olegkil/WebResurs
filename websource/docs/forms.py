from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, BooleanField, CheckboxInput, FileField, \
    ClearableFileInput


class ArticlesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date', 'upload_file', 'is_published']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control'
            })

        }