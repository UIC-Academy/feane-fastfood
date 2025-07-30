from django.urls import path
from foods.views import IndexView, MenuView, AboutView, BookView, booking_create_view



urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("menu/", MenuView.as_view(), name="menu"),
    path("about/", AboutView.as_view(), name="about"),
    path("book/", BookView.as_view(), name="book"),
    path("booking/create/", booking_create_view, name="booking-create")
]