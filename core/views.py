from django.views.generic import ListView
from .models import Spesa

class HomePageView(ListView):
    template_name = 'home.html'
    model = Spesa
