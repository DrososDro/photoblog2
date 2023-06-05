from django import forms
from .models import Account


class UserModelForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
        exclude = [
            "password",
            "is_admin",
            "is_superadmin",
            "is_staff",
            "is_active",
            "permissions",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control text-3 h-auto py-2"})
