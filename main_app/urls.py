from django.urls import path
from . import views

urlpatterns = [
    path('', views.criar_evento, name='home'),
]
