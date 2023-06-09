from django import forms
from .models import BlogInfo


class BlogInfoForm(forms.ModelForm):
    class Meta:
        model = BlogInfo
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(BlogInfoForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control text-3 h-auto py-2",
                }
            )
