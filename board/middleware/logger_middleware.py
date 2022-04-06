from django.core.exceptions import PermissionDenied
import datetime


class Logger:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        http_method = request.method
        url = request.path
        date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        with open('log.txt', 'a') as f:
            f.write(date_time + ' ' + http_method + ' ' + url + '\n')
        response=self.get_response(request)

        return response


