from time import sleep

from django.http import HttpResponse


def slow_view(request):
    sleep(1)
    return HttpResponse("Done", status=200)
