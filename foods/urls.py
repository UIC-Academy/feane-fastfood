from django.urls import path

from foods.views import IndexView, MenuView


urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("menu/", MenuView.as_view(), name="menu")
]
