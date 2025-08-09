from tkinter.font import names

from django.urls import path
from .views import (home, home2, home_d, home2_d,
                    about, random_view, random_view2, random_view3,
                    new_test_redirect)


urlpatterns = [
    path('home/', home, name="h_page"),
    path('home_d/<number>', home_d),
    path('home2/', home2),
    path('home2_d/<number>', home2_d),
    path('about/', about, name="about_p"),
    path('random_view/<int:start>/<int:end>', random_view2, name="r2"),
    path('random_view/', random_view, name="r1"),
    path('random_view/<int:start>/<int:end>/<int:turns>', random_view3, name="r3"),
    path('red_test/', new_test_redirect, name="new_test"),
]