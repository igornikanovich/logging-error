from django.shortcuts import render, redirect
from django.views.generic import View, CreateView

from .forms import UserForm


class RedirectView(View):

    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('app_list')
            else:
                return redirect('app_list')
        else:
            return redirect('login')


class UserRegistrationView(CreateView):

    def get(self, request, *args, **kwargs):
        registered = False
        return render(request, 'registration/registration.html', {'user_form': UserForm,
                                                                  'registered': registered})

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return render(request, 'registration/registration.html',
                          {'user_form': user_form,
                           'registered': registered})
        return render(request, 'registration/registration.html', {'user_form': user_form})
