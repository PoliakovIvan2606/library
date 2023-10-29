from django import forms
from .models import Book


class PostBook (forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'book', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form'}),
            'author': forms.TextInput(attrs={'class':'form'}),
            'book': forms.FileInput(attrs={'class':'form'}),
            # 'category': forms.Input(attrs={'class':'form'})
        }