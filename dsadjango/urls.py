"""dsadjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path
from random import randint

def hello_world( request: HttpRequest)->HttpResponse:
    return (HttpResponse("Hello World. <br> <a href='weather'>Get weather</a    ></br>"))


def show_weather(request: HttpRequest)->HttpResponse:
    temperature = randint(-40,40)
    feel = "OK"
    if temperature < 0:
        feel = "cold"
    if temperature < -10:
        feel = "terribly cold"

    return (HttpResponse(f"Today is {temperature} celsius degree. It is {feel}! <br><a href='hello'>main page</a></br>"))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('hello', hello_world),
    path('weather', show_weather),
]
