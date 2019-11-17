# def charts(request):
#     date = list()
#     error_count = list()
#
#     first_error_date = Error.objects.all().order_by('date').first()
#     last_error_date = Error.objects.all().order_by('date').last()
#     first_date = first_error_date.date.date()
#     last_date = last_error_date.date.date()
#     delta_date = last_date - first_date
#     total_days = delta_date.days + 1
#
#     all_errors = Error.objects.all()
#
#     for day_number in range(total_days):
#         current_date = (first_date + dt.timedelta(days=day_number))
#         date.append('%s' % current_date)
#         count_errors_in_day = 0
#         for error in all_errors:
#             if error.date.date() == current_date:
#                 count_errors_in_day += 1
#         error_count.append(count_errors_in_day)
#
#     return render(request, 'test.html', {
#         'date': json.dumps(date),
#         'error_count': json.dumps(error_count),
#     })
