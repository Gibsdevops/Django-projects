from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class ServicesPageView(TemplateView):
    template_name = 'services.html'