from django import forms
from .models import Article


class AddArticleForm(forms.ModelForm):
    """

    add_tags = forms.CharField(
        label="Add Tags",
        widget=forms.TextInput(
            attrs={
                "class": "form-control text-3 h-auto py-2",
                "placeholder": "#YourTag #YourTag",
                "pattern": "^(#(\w+)\s*)+$",
            }
        ),
    )
    """

    class Meta:
        model = Article
        fields = ["title", "description", "tags"]
        widgets = {
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"})
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

    def _save_m2m(self):
        return super()._save_m2m()
        """
        if add_tags:
            tags = add_tags.replace("#", " ").split()
        for tag in tags:
            try:
                tag_instance, _ = Tag.objects.get_or_create(title=tag)
                self.instance.tags.add(tag_instance)
            except Exception:
                pass
            print(self.instance.tags.all())
        """
