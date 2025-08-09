from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),  # /core/
    path('about/', views.about, name='about'),
    path('random/', views.random_number_view, name='random1'),                  # одно число 0–100 (HttpResponse)
    path('random/<int:start>/<int:end>/', views.random_view2, name='random2'),  # одно число в диапазоне (шаблон)
    path('random_view/<int:start>/<int:end>/<int:turns>/',                      # как на скрине
         views.random_view3, name='random3'),
    path('calc/', views.calculator_view, name='calc'),
]


# python manage.py runserver