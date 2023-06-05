from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, Group
from .models import Account, Perm, MultipleAccountImages
from django import forms
from django.core.exceptions import ValidationError

# Register your models here.


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = Account
        fields = ["email", "name"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {"class": "form-control text-3 h-auto py-2"},
            )


class MyCustomAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ("email", "last_login", "date_joined")
    list_filter = ()
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "name",
                    "surname",
                    "phone",
                    "short_intro",
                    "bio",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_admin",
                    "is_superadmin",
                    "is_active",
                    "permissions",
                )
            },
        ),
        ("Details", {"fields": ("last_login", "date_joined")}),
    )
    filter_horizontal = ()
    search_fields = ("email",)
    readonly_fields = ("last_login", "date_joined")
    ordering = ["email"]


admin.site.unregister(Group)
admin.site.register(Account, MyCustomAdmin)
admin.site.register(Perm)
admin.site.register(MultipleAccountImages)
