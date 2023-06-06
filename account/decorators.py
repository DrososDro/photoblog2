from django.shortcuts import redirect


def authenticated_user(view_func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return redirect("login")

    return wrap


def unauthenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return redirect("home")

    return wrapper


def permisions_required(perm_list: list = None):
    def decorator(view_func):
        def wraper(request, *args, **kwargs):
            if perm_list:
                permissions = request.user.permissions.all().values_list(
                    "name", flat=True
                )
                for perm in perm_list:
                    if perm in permissions:
                        return view_func(request, *args, **kwargs)
                return redirect("home")

            return redirect("home")

        return wraper

    return decorator
