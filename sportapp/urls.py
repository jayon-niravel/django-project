
from django.urls import path
from .views import Home

urlpatterns = [
    path('sportapp/', Home, name = 'sportapp')
]
