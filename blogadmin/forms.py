from django import forms
from .models import BlogInfo


class BlogInfoForm(forms.ModelForm):
    class Meta:
        model = BlogInfo
        fields = "__all__"
