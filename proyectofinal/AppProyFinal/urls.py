
from django.urls import path
from AppProyFinal.views import inicio

urlpatterns = [
    path('inicio/',inicio, name='inicio')
]
