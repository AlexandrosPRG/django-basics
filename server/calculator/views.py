from django.db.models.expressions import result
from django.shortcuts import render
from django.http import HttpResponse


def calc_view(request):
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    operation = request.GET.get("operation")

    result = None
    if num1 is not None and num2 is not None:
        if operation == "+":
            result = int(num1) + int(num2)
        
        if operation == "-":
            result = int(num1) - int(num2)

    return render(request, "calc.html", {"result": result})


def showcase_plus(request, num1, num2):
    return HttpResponse(f"Vysledok: {num2+num1}")