ACCESS_CONTROL_ALLOW_ORIGIN = "Access-Control-Allow-Origin"
ACCESS_CONTROL_EXPOSE_HEADERS = "Access-Control-Expose-Headers"
ACCESS_CONTROL_ALLOW_CREDENTIALS = "Access-Control-Allow-Credentials"
ACCESS_CONTROL_ALLOW_HEADERS = "Access-Control-Allow-Headers"
ACCESS_CONTROL_ALLOW_METHODS = "Access-Control-Allow-Methods"
ACCESS_CONTROL_MAX_AGE = "Access-Control-Max-Age"


class AppMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response[ACCESS_CONTROL_ALLOW_ORIGIN] = "*"
        response[ACCESS_CONTROL_ALLOW_HEADERS] = "*"
        # response[ACCESS_CONTROL_ALLOW_METHODS] = "*"
        return response
