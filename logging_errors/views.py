import json
from uuid import uuid4
import datetime as dt

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Application, Error


class ApplicationListView(ListView):
    template_name = 'applications.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        application_list = Application.objects.filter(author=self.request.user)
        paginator = Paginator(application_list, self.paginate_by)
        page = request.GET.get('page')
        try:
            application_list = paginator.page(page)
        except PageNotAnInteger:
            application_list = paginator.page(1)
        except EmptyPage:
            application_list = paginator.page(paginator.num_pages)
        return render(request, 'applications.html', {'application_list': application_list})

    @staticmethod
    def post(request):
        new_application = request.POST.get('addnewapp')
        if len(str(new_application)) > 0:
            token = uuid4()
            application = Application.objects.create(name=new_application, token=token, author=request.user)
            application.save()
            return redirect('app_list')
        else:
            return redirect('app_list')


class ErrorApplicationListView(ListView):
    model = Error
    template_name = 'application_detail.html'
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        application = Application.objects.get(id=self.kwargs['id'])
        app_name = application.name
        app_token = application.token
        errors_set = Error.objects.filter(app_id=self.kwargs['id']).values_list('type', flat=True).distinct()
        type_error = request.GET.get('type')
        if type_error:
            error_list = Error.objects.filter(app_id=self.kwargs['id']).filter(type=type_error).order_by('-date')
            first_error_date = error_list.last()
            last_error_date = error_list.first()
            error_list_charts = error_list
            paginator = Paginator(error_list, self.paginate_by)
            page = request.GET.get('page')
            try:
                error_list = paginator.page(page)
            except PageNotAnInteger:
                error_list = paginator.page(1)
            except EmptyPage:
                error_list = paginator.page(paginator.num_pages)
            first_date = first_error_date.date.date()
            last_date = last_error_date.date.date()
            time = list()
            count_errors = list()
            if first_date == last_date:
                for hour in range(24):
                    time.append('%s' % hour)
                    count_hour_errors = 0
                    for error in error_list_charts:
                        if error.date.hour == hour:
                            count_hour_errors += 1
                    count_errors.append(count_hour_errors)
            else:
                delta_dates = last_date - first_date
                total_days = delta_dates.days + 1
                for day_number in range(total_days):
                    current_date = (first_date + dt.timedelta(days=day_number))
                    time.append('%s' % current_date)
                    count_day_errors = 0
                    for error in error_list_charts:
                        if error.date.date() == current_date:
                            count_day_errors += 1
                    count_errors.append(count_day_errors)
                time.reverse()
                count_errors.reverse()
        else:
            error_list, time, count_errors = None, None, None
        return render(request, 'application_detail.html', {'error_set': errors_set,
                                                           'error_list': error_list,
                                                           'error_type': type_error,
                                                           'app_name': app_name,
                                                           'app_token': app_token,
                                                           'date': json.dumps(time),
                                                           'count_errors': json.dumps(count_errors),
                                                           })
