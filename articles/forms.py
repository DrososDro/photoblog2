from django import forms
from .models import Article


class AddArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "description", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "form-check-input",
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(AddArticleForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name in ["tags", "add_tags", "images"]:
                pass
            else:
                field.widget.attrs.update(
                    {
                        "class": "form-control text-3 h-auto py-2",
                        "placeholder": f"Enter {name}".title(),
                    }
                )
