from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from market.models import Car
# Create your views here.

def show_cars(request: HttpRequest)->HttpResponse:
    context = {
        "cars":Car.objects.all()

    }
    return render(request, "cars.html", context)