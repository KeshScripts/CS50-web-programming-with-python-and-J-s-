from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("add", views.add, name="add"),
   path('<int:Flight_id>', views.flight, name="Flight"),
   path('<int:Flight_id>/book', views.book, name="book")
   
]