from django.shortcuts import render
from .models import BlogInfo
from django.views.generic import UpdateView
from .forms import BlogInfoForm
from django.urls import reverse
from django.shortcuts import redirect
from .utils import multiple_blog_image_add

# Create your views here.


class UpdateBlog(UpdateView):
    model = BlogInfo
    form_class = BlogInfoForm
    template_name = "blogadmin/admin_form.html"

    def get_success_url(self):
        return reverse("update-user", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        queryset = BlogInfo.objects.first()
        return queryset

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        multiple_blog_image_add(self.request, self.object)
        return redirect(self.get_success_url())
