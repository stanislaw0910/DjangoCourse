import datetime
from django.core.exceptions import SuspiciousOperation


class AntiSpamMiddleware:
    TIME = 10
    COUNT = 3

    def __init__(self, get_response):
        self.get_response = get_response
        self.count = 0
        self.cur_time = datetime.datetime.now()
        self.ips = dict()

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        if (datetime.datetime.now() - self.cur_time).seconds > AntiSpamMiddleware.TIME:
            self.cur_time = datetime.datetime.now()
            for key in self.ips.keys():
                self.ips[key] = 0

        if not self.ips.get(ip):
            self.ips[ip] = 1
        else:
            self.ips[ip] = self.ips[ip] + 1
        print(self.ips)
        if self.ips[ip] > AntiSpamMiddleware.COUNT:
            raise SuspiciousOperation

        response = self.get_response(request)
        return response
