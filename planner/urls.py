from . import views
from django.urls import path

urlpatterns = [
    path('meal', views.meal_view),
]