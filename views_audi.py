from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

orders = []


cars = [
    {
        "id": 1,
        "purchased":False,
        "model": "A6",
        "image":"https://thumb.tildacdn.com/tild3836-3936-4134-a433-353663656330/-/resize/520x/-/format/webp/2019.png"
    },
    {
        "id": 2,
        "purchased":False,
        "model": "A7",
        "image": "https://thumb.tildacdn.com/tild3962-6335-4139-b962-386636356338/-/resize/520x/-/format/webp/2019.png"
    },
    {
        "id": 3,
        "purchased": False,
        "model": "A8",
        "image": "https://thumb.tildacdn.com/tild3764-6131-4966-b237-393635633965/-/resize/520x/-/format/webp/2019.png"
    },
    {
        "id": 4,
        "purchased": False,
        "model": "Q3",
        "image": "https://thumb.tildacdn.com/tild3032-6439-4663-b965-633332653537/-/resize/520x/-/format/webp/2019.png"
    },
]





def audi(request:HttpRequest)->HttpResponse:
    global cars
    context = {"cars":cars, "name":"Timur"}
    return  render(request, "cars.html", context)


def audi_purchase(request:HttpRequest, id_:int)->HttpResponse:
    global cars
    cars_with_id_match = [car for car in cars if car["id"] == id_]
    car = cars_with_id_match[0]
    if request.method=="POST":
        orders.append(
            {
            "car":car,
            "name":request.POST.get("name"),
            "phone": request.POST.get("phone"),
            "email": request.POST.get("email"),
             }
        )
        print(orders)
        car["purchased"] = True
        return HttpResponseRedirect("/audi")
    return HttpResponse(
        f"""
        <h3> Great! you are going to purchase{car["model"]} </h3>
        <form method="POST">
            <laber for "name"> Your name</label>
            <input id="name" name="name" required><br>
            <laber for "phone"> Your phone</label>
            <input id="phone" name="phone"required><br>
            <laber for "email"> Your email</label>
            <input id="email" name="email" type="email" required><br>
            <button type="submit">Submit</button><br>
        </form>
        """

    )
    #return HttpResponseRedirect("/audi")
    # return HttpResponse(f"Car with id {id_} is sold")