from django.shortcuts import render
from .models import UserProfile

def allowed_roles(roles=None):

    if roles is None:
        roles = ['admin']

    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            if not request.user.is_authenticated:

                return render(
                    request,
                    'login_requerido.html'
                )

            try:

                profile = UserProfile.objects.get(
                    user=request.user
                )

            except UserProfile.DoesNotExist:

                return render(
                    request,
                    'sin_perfil.html'
                )

            if profile.role in roles:

                return view_func(
                    request,
                    *args,
                    **kwargs
                )

            return render(
                request,
                'acceso_denegado.html'
            )

        return wrapper

    return decorator