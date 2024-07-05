from django.urls import path
from . import views

urlpatterns = [
    path('projections/', views.index, name='projections'),
]