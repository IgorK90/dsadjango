from random import randint

from django.http import HttpResponse, HttpRequest


def show_weather(request: HttpRequest)->HttpResponse:
    temperature = randint(-40,40)
    feel = "OK"
    if temperature < 0:
        feel = "cold"
    if temperature < -10:
        feel = "terribly cold"

    return (HttpResponse(f"Today is {temperature} celsius degree. It is {feel}! <br><a href='hello'>main page</a></br>"))
