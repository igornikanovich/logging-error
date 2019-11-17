import datetime
import datetime as dt

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, DetailView
from django.db.models import Count, Q

import json
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


class ApplicationDetailView(DetailView):
    model = Application
    template_name = 'application_detail.html'

    def get(self, request, *args, **kwargs):
        errors_set = Error.objects.filter(app_id=self.kwargs['id']).values_list('type', flat=True).distinct()
        type_error = request.GET.get('type')
        error_list = Error.objects.filter(type=type_error).order_by('-date')
        date = list()
        count_errors = list()
        first_error_date = Error.objects.filter(type=type_error).order_by('date').first()
        last_error_date = Error.objects.filter(type=type_error).order_by('date').last()
        first_date = first_error_date.date.date()
        last_date = last_error_date.date.date()
        delta_dates = last_date - first_date
        total_days = delta_dates.days + 1
        for day_number in range(total_days):
            current_date = (first_date + dt.timedelta(days=day_number))
            date.append('%s' % current_date)
            count_day_errors = 0
            for error in error_list:
                if error.date.date() == current_date:
                    count_day_errors += 1
            count_errors.append(count_day_errors)
        return render(request, 'application_detail.html', {'errors_set': errors_set,
                                                           'errors_list': error_list,
                                                           'date': json.dumps(date),
                                                           'count_errors': json.dumps(count_errors),
                                                           })


# delete
class ErrorListView(ListView):

    def get(self, request, *args, **kwargs):
        errors_set = Error.objects.values_list('type', flat=True).distinct()
        return render(request, 'errors.html', {'error_list': errors_set})


# delete
class ErrorDetailView(ListView):

    def get(self, request, *args, **kwargs):
        error_list = Error.objects.filter(id=self.kwargs['id'])
        return render(request, 'errors_detail.html', {'error_list': error_list})

