from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse

from foods.models import Category, Food, Feedback
from foods.forms import BookingForm

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        foods = Food.objects.filter(is_active=True)
        feedbacks = Feedback.objects.all()
        form = Feedback()

        kwargs["categories"] = categories
        kwargs["foods"] = foods
        kwargs["feedbacks"] = feedbacks
        kwargs["form"] = BookingForm()
        return super().get_context_data(**kwargs)

class MenuView(TemplateView):
    template_name = "menu.html"

class AboutView(TemplateView):
    template_name = "about.html"

class BookView(TemplateView):
    template_name = "book.html"


def booking_create_view(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponseBadRequest("Invalid form")

    else:
        form = BookingForm()

    return render(request, "index.html", {"form": form})