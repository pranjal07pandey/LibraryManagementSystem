from django import forms
from .models import BookDetail


class NewBookForm(forms.ModelForm):
    class Meta:
        model = BookDetail
        fields = ('b_id', 'author', 'title', 'quantity', 'published_date', 'genre')


