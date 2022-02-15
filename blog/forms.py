from django import forms
from .models import Post


class PostSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

