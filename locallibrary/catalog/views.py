from django.shortcuts import render, HttpResponse
from prometheus_client import Counter

# Create your views here.
c = Counter('my_failures', 'Description of counter')


def counter(requests):
    c.inc()  # Increment by 1
    c.inc(1.6)  # Increment by given value
    return HttpResponse("counter {}".format(c.collect()))


