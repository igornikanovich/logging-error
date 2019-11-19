import functools
import requests
import sys
import traceback
import json
from datetime import datetime

import crashlytics.configSDK as config


class RequestsHTTPTransport:

    def __init__(self, url, token):
        self.url = url
        self.token = token

    def send(self, data):
        data = json.dumps(data)
        headers = {"content-type": "application/json"}
        url = '{}{}/'.format(self.url, self.token)
        requests.post(url, data=data, headers=headers)


def error_handler(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception:
            error_type, error_message, error_traceback = sys.exc_info()
            error_date = datetime.now().isoformat()
            trace_back = traceback.extract_tb(error_traceback)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(
                    "File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
            error_data = {"type": error_type.__name__,
                          "date": error_date,
                          "message": '%s' % error_message,
                          "stacktrace": "".join(stack_trace)}
            RequestsHTTPTransport(config.url, config.token).send(error_data)
    return wrapper
