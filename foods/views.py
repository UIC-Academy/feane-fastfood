from django.shortcuts import render
from django.views.generic import TemplateView

from foods.models import Category

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        kwargs["categories"] = categories
        return super().get_context_data(**kwargs)

class MenuView(TemplateView):
    template_name = "menu.html"

class AboutView(TemplateView):
    template_name = "about.html"

class BookView(TemplateView):
    template_name = "book.html"