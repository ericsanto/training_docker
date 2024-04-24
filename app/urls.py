from django.urls import path
from .views import home, sanit_kubernetes

urlpatterns = [
    path('inicio/', home, name='home'),
    path('teste/', sanit_kubernetes, name='teste'),
]
