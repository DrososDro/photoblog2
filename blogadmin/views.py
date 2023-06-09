from django.shortcuts import render
from .models import BlogInfo, MultipleBlogImages
from django.views.generic import UpdateView, DeleteView, ListView
from .forms import BlogInfoForm
from django.urls import reverse
from django.shortcuts import redirect
from .utils import multiple_blog_image_add
from account.models import Account

# Create your views here.


class UpdateBlog(UpdateView):
    model = BlogInfo
    form_class = BlogInfoForm
    template_name = "blogadmin/admin_form.html"

    def get_success_url(self):
        return reverse("blog")

    def get_object(self, queryset=None):
        queryset = BlogInfo.objects.first()
        return queryset

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        multiple_blog_image_add(self.request, self.object)
        return redirect(self.get_success_url())


class DeleteBlogImage(DeleteView):
    model = MultipleBlogImages
    template_name = "delete.html"
    extra_context = {"text": "This Picture"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["action"] = reverse(
            "delete-blog-image", kwargs={"pk": self.kwargs["pk"]}
        )
        return context

    def get_success_url(self):
        return reverse("blog")


"""

class UsersView(ListView):
    model = Account
    paginate_by = 4
    template_name = "blogadmin/users.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["search"] = True
        context["search_action"] = reverse("user-admin")
        context["search_name"] = "q_user"

        return context

    def get_queryset(self):
        if "q_user" in self.request.GET:
            q_user = self.request.GET.get("q_user")
            queryset = (
                Account.objects.distinct()
                .filter(email__icontains=q_user)
                .exclude(is_superadmin=True)
            )

            return queryset
        else:
            return super().get_queryset().exclude(is_superadmin=True)

"""
