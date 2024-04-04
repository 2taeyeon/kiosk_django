from django.http import HttpResponse
from django.views import generic
from .models import Drink, DrinkChoice


def index(request):
    return HttpResponse("kiosk index")


class DrinkListView(generic.ListView):
    model = Drink
    template_name = "kiosk/drink_list.html"
    context_object_name = "drinks"


class DrinkDetailView(generic.DetailView):
    model = DrinkChoice
    template_name = "kiosk/drink_detail.html"
    context_object_name = "drink"
