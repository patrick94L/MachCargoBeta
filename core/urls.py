from django.urls import path
from . import views

app_name = "CORE"

urlpatterns = [
    path('', views.index, name='index'),
    # Otras rutas y vistas aquí
]

