from django.shortcuts import render, redirect
from django.http import HttpResponse
from random import randint

def home(request):
    return HttpResponse("Hello World!")

def home2(request):
    return render(request, "home2.html")

def home_d(request, number):
    return HttpResponse(f"Hello World! {number}")

def home2_d(request, number):
    return render(request, "home2.html", {"number": number})

def about(request):
    return render(request, "about.html")

def random_view(request):
    number = randint(0, 100)
    return render(request, "random_page.html", {"number": number})

def random_view2(request, start, end):
    number = randint(start, end)
    return render(request, "random_page.html", {"number": number})

def random_view3(request, start, end, turns):
    numbers = [randint(start, end) for _ in range(turns)]
    print(numbers)
    return render(request, "random_page2.html", {"numbers": numbers})

def random_number_view(request):
    number = randint(0, 100)
    return HttpResponse(f"Drawn number: {number}")

def new_test_redirect(request):
    print("Sme v testovani redirectu")
    return redirect("r3", 300, 600, 15)

# ---------------------------
# Calculator
# ---------------------------
def calculator_view(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    result = None

    if num1 and num2:
        try:
            result = int(num1) + int(num2)
        except ValueError:
            result = "Ошибка: введите числа"

    return render(request, "calculator.html", {
        "num1": num1 or "",
        "num2": num2 or "",
        "result": result
    })