from time import sleep


class ResponseDelay:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        sleep(1)

        return response
