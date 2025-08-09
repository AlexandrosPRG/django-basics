from django.urls import path
from .views import calc_view, showcase_plus


urlpatterns = [
    path('', calc_view, name="calc"),
    path('show_p/<int:num1>/<int:num2>', showcase_plus),
]