from django import forms
from .models import Account, MultipleAccountImages


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

    # profile_pic = forms.ModelChoiceField(queryset=Account.image_object.all())
    # print(Account.image_object.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control text-3 h-auto py-2"})

        self.fields["profile_pic"].queryset = MultipleAccountImages.objects.filter(
            account=self.instance
        )
