from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class MenuView(TemplateView):
    template_name = "menu.html"