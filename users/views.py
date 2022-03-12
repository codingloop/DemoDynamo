from django.shortcuts import render


# Create your views here.
def handle_callback(req):
    from django.http import HttpResponse
    print(req.GET)

    return HttpResponse("Hi".encode())
