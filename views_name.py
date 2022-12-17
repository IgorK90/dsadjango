from django.http import HttpResponse, HttpRequest


def name(request: HttpRequest)->HttpResponse:

    if request.method=="POST":
        name = request.POST.get("name", "")
        age = int(request.POST.get("age",""))
        return HttpResponse(
            f"""Thank You, {name},<br> 
            You are {age} year(s) old
            """)
    return HttpResponse(
        f"""
        <form method="POST">
            <label for="name">What is your name</label>
            <input id="name" name="name" value="Bill"><br>
            <label for="age">What is your age</label>
            <input id="age" name="age" type="number" value=50><br>
            <button type="submit">Submit</button>
        </form>
        
        
        
        """
    )