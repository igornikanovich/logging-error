from django.shortcuts import render, redirect
from django.views.generic import View

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


# class UserRegistrationView(View):


def registration(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
    else:
        user_form = UserForm()
    return render(request, 'registration/registration.html',
                  {'user_form': user_form,
                   'registered': registered})
