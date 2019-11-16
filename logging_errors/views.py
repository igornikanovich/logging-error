from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView

from uuid import uuid4

from .models import Application, Error


class ApplicationListView(ListView):
    queryset = Application.objects.all()
    template_name = 'applications.html'

    @staticmethod
    def post(request):
        new_application = request.POST.get('addnewapp')
        if len(str(new_application)) > 0:
            token = uuid4()
            application = Application.objects.create(name=new_application, token=token)
            application.save()
            return redirect('app_list')
        else:
            return redirect('app_list')


class ErrorListView(ListView):
    queryset = Error.objects.all()
    template_name = 'test.html'
